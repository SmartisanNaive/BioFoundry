from __future__ import annotations

import json
from typing import Any

import httpx
import pytest
from fastmcp import Client
from typer.testing import CliRunner

from biofoundry_cli.cli import cli
from biofoundry_cli.cli.mcp import build_builtin_synpan_mcp_config, merge_builtin_mcp_configs
from biofoundry_cli.synpan.client import SynPanClient
from biofoundry_cli.synpan.mcp_server import create_mcp_server
from biofoundry_cli.synpan.models import (
    SUCCESS_CODE,
    FunctionRequest,
    SetParameter,
)
from biofoundry_cli.synpan.platform_client import SynPanPlatformClient
from biofoundry_cli.synpan.platform_mcp_server import add_platform_tools


def _json_request_body(request: httpx.Request) -> Any | None:
    if not request.content:
        return None
    return json.loads(request.content.decode("utf-8"))


@pytest.mark.asyncio
async def test_synpan_client_uses_standard_endpoints_and_payloads() -> None:
    calls: list[tuple[str, str, Any | None]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append((request.method, request.url.path, _json_request_body(request)))
        return httpx.Response(
            200,
            json={"code": SUCCESS_CODE, "message": "Success", "data": {"accepted": True}},
        )

    client = SynPanClient(
        base_url="http://device.local/api/",
        transport=httpx.MockTransport(handler),
    )

    info = await client.get_info()
    heartbeat = await client.get_heartbeat()
    result = await client.run_function(
        FunctionRequest(
            function_name="absorbance",
            function_param={"wavelength": 450},
            instruction_id="inst-001",
            labware_info={"LabwareName": "plate-96"},
            equipment_name="reader",
            nest_id="Plate1",
            user_id="user-1",
            task_id="task-1",
        )
    )

    assert info.ok
    assert heartbeat.ok
    assert result.ok
    assert calls == [
        ("GET", "/api/Info", None),
        ("GET", "/api/HeartBeat", None),
        (
            "POST",
            "/api/Function",
            {
                "functionName": "absorbance",
                "functionParam": {"wavelength": 450},
                "instructionId": "inst-001",
                "labwareInfo": {"LabwareName": "plate-96"},
                "equipmentName": "reader",
                "nestId": "Plate1",
                "userId": "user-1",
                "taskId": "task-1",
            },
        ),
    ]


@pytest.mark.asyncio
async def test_synpan_client_set_parameters_converts_snake_case() -> None:
    payloads: list[Any | None] = []

    def handler(request: httpx.Request) -> httpx.Response:
        payloads.append(_json_request_body(request))
        return httpx.Response(200, json={"code": SUCCESS_CODE, "message": "Success", "data": True})

    client = SynPanClient(
        base_url="http://device.local",
        transport=httpx.MockTransport(handler),
    )

    response = await client.set_parameters(
        [SetParameter(set_name="target_temperature", set_value="37")]
    )

    assert response.ok
    assert payloads == [[{"setName": "target_temperature", "setValue": "37"}]]


@pytest.mark.asyncio
async def test_synpan_client_extracts_capabilities_from_info() -> None:
    register_info = {
        "basicInfo": {"equipmentName": "酶标仪"},
        "advancedInfo": {
            "equipmentFunctions": [{"functionName": "absorbance"}],
            "equipmentOperations": [{"operationName": "reset"}],
            "equipmentSetInfos": [{"setName": "target_temperature"}],
            "equipmentGetInfos": [{"getName": "status"}],
            "equipmentNests": [{"nestName": "Plate1"}],
            "equipmentEnterAndExit": {"enterAndExitName": "plate_in"},
        },
    }

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/Info"
        return httpx.Response(
            200,
            json={"code": SUCCESS_CODE, "message": "Success", "data": register_info},
        )

    client = SynPanClient(
        base_url="http://device.local",
        transport=httpx.MockTransport(handler),
    )

    response = await client.list_capabilities()

    assert response.ok
    data = response.data
    assert data is not None
    assert data["basic_info"]["equipmentName"] == "酶标仪"
    assert data["functions"] == [{"functionName": "absorbance"}]
    assert data["operations"] == [{"operationName": "reset"}]
    assert data["sets"] == [{"setName": "target_temperature"}]
    assert data["gets"] == [{"getName": "status"}]
    assert data["nests"] == [{"nestName": "Plate1"}]
    assert data["enter_and_exit"] == {"enterAndExitName": "plate_in"}


@pytest.mark.asyncio
async def test_synpan_client_returns_structured_errors() -> None:
    missing_base = SynPanClient(env={})
    missing_response = await missing_base.get_info()

    assert not missing_response.ok
    assert missing_response.error_type == "configuration"

    def http_error_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            500,
            json={"code": "message.common.server.error", "message": "Device failed"},
        )

    http_error_client = SynPanClient(
        base_url="http://device.local",
        transport=httpx.MockTransport(http_error_handler),
    )
    http_error_response = await http_error_client.get_info()

    assert not http_error_response.ok
    assert http_error_response.http_status == 500
    assert http_error_response.synpan_code == "message.common.server.error"
    assert http_error_response.message == "Device failed"
    assert http_error_response.error_type == "http"

    def network_error_handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection refused", request=request)

    network_error_client = SynPanClient(
        base_url="http://device.local",
        transport=httpx.MockTransport(network_error_handler),
    )
    network_error_response = await network_error_client.get_info()

    assert not network_error_response.ok
    assert network_error_response.error_type == "network"


@pytest.mark.asyncio
async def test_synpan_mcp_server_registers_and_calls_tools() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/Get"
        return httpx.Response(
            200,
            json={
                "code": SUCCESS_CODE,
                "message": "Success",
                "data": [{"getName": "status", "getValue": "idle"}],
            },
        )

    client = SynPanClient(
        base_url="http://device.local",
        transport=httpx.MockTransport(handler),
    )
    server = create_mcp_server(client)

    tool_names = set(await server.get_tools())
    assert {
        "synpan_get_info",
        "synpan_list_capabilities",
        "synpan_get_heartbeat",
        "synpan_get_status",
        "synpan_run_function",
        "synpan_run_operation",
        "synpan_set_parameters",
        "synpan_enter_and_exit",
    } <= tool_names

    async with Client(server) as mcp_client:
        result = await mcp_client.call_tool("synpan_get_status", {})

    assert result.data["ok"] is True
    assert result.data["data"] == [{"getName": "status", "getValue": "idle"}]


@pytest.mark.asyncio
async def test_synpan_platform_client_uses_post_and_third_party_token_header() -> None:
    calls: list[tuple[str, str, str | None, Any | None]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(
            (
                request.method,
                request.url.path,
                request.headers.get("ThirdPartyToken"),
                _json_request_body(request),
            )
        )
        return httpx.Response(200, json={"code": 200, "message": "ok", "data": {"accepted": True}})

    client = SynPanPlatformClient(
        base_url="http://platform.local/api",
        token="token-123",
        transport=httpx.MockTransport(handler),
    )

    response = await client.post(SynPanPlatformClient.PATHS["getWorkCellList"], {})

    assert response.ok is True
    assert calls == [
        ("POST", "/api/thirdParty/mcp/getWorkCellList", "token-123", {}),
    ]


@pytest.mark.asyncio
async def test_synpan_platform_client_uses_new_env_vars() -> None:
    calls: list[tuple[str, str]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append((request.method, request.url.path))
        return httpx.Response(200, json={"code": 200, "message": "ok", "data": {}})

    client = SynPanPlatformClient(
        env={
            "SYNPAN_PLATFORM_BASE_URL": "http://new.local",
            "SYNPAN_PLATFORM_TOKEN": "new-token",
        },
        transport=httpx.MockTransport(handler),
    )

    response = await client.post(SynPanPlatformClient.PATHS["getWorkCellList"], {})

    assert response.ok is True
    assert calls == [("POST", "/thirdParty/mcp/getWorkCellList")]


@pytest.mark.asyncio
async def test_synpan_platform_client_falls_back_to_xingpan_env_vars() -> None:
    calls: list[tuple[str, str]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append((request.method, request.url.path))
        return httpx.Response(200, json={"code": 200, "message": "ok", "data": {}})

    client = SynPanPlatformClient(
        env={
            "XINGPAN_BASE_URL": "http://legacy.local",
            "XINGPAN_TOKEN": "legacy-token",
        },
        transport=httpx.MockTransport(handler),
    )

    response = await client.post(SynPanPlatformClient.PATHS["getWorkCellList"], {})

    assert response.ok is True
    assert calls == [("POST", "/thirdParty/mcp/getWorkCellList")]


@pytest.mark.asyncio
async def test_synpan_platform_mcp_server_registers_and_calls_tools() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/thirdParty/mcp/getWorkCellList"
        return httpx.Response(
            200,
            json={
                "code": 200,
                "message": "ok",
                "data": [{"workCellId": "wc-1", "cellName": "cell"}],
            },
        )

    client = SynPanPlatformClient(
        base_url="http://platform.local",
        token="token-123",
        transport=httpx.MockTransport(handler),
    )
    server = create_mcp_server(platform_client=client)

    tool_names = set(await server.get_tools())
    assert {"getWorkCellList", "createOrder", "operateOrder", "getTaskInfo"} <= tool_names

    async with Client(server) as mcp_client:
        result = await mcp_client.call_tool("getWorkCellList", {})

    assert result.data["ok"] is True
    assert result.data["data"] == [{"workCellId": "wc-1", "cellName": "cell"}]


@pytest.mark.asyncio
async def test_synpan_platform_tools_can_be_added_to_a_bare_mcp() -> None:
    from fastmcp import FastMCP

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"code": 200, "message": "ok", "data": []})

    client = SynPanPlatformClient(
        base_url="http://platform.local",
        token="token-123",
        transport=httpx.MockTransport(handler),
    )
    mcp = FastMCP("test")
    add_platform_tools(mcp, client)

    tool_names = set(await mcp.get_tools())
    assert "getWorkCellList" in tool_names


def test_builtin_synpan_mcp_config_points_to_cli_module() -> None:
    config = build_builtin_synpan_mcp_config()

    assert config["mcpServers"]["synpan"]["args"] == ["-m", "biofoundry_cli.cli", "synpan-mcp"]


def test_merge_builtin_synpan_mcp_config_skips_existing_server() -> None:
    existing = [{"mcpServers": {"synpan": {"command": "custom", "args": []}}}]

    merged = merge_builtin_mcp_configs(existing)

    assert merged == existing


def test_merge_builtin_synpan_mcp_config_can_disable_default() -> None:
    merged = merge_builtin_mcp_configs([], disable_builtin_synpan=True)

    assert merged == []


def test_synpan_mcp_cli_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["synpan-mcp", "--help"])

    assert result.exit_code == 0
    assert "Run the unified SynPan MCP server" in result.stdout


def test_xingpan_mcp_cli_command_removed() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["xingpan-mcp", "--help"])

    assert result.exit_code != 0
    output = result.stdout + result.stderr
    assert "No such command" in output or "Missing command" in output
