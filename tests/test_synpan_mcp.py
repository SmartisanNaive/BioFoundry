from __future__ import annotations

import json
from typing import Any

import httpx
import pytest
from fastmcp import Client
from typer.testing import CliRunner

from biofoundry_cli.cli import cli
from biofoundry_cli.synpan.client import SynPanClient
from biofoundry_cli.synpan.mcp_server import create_mcp_server
from biofoundry_cli.synpan.models import (
    SUCCESS_CODE,
    FunctionRequest,
    SetParameter,
)


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
    assert response.data["basic_info"]["equipmentName"] == "酶标仪"
    assert response.data["functions"] == [{"functionName": "absorbance"}]
    assert response.data["operations"] == [{"operationName": "reset"}]
    assert response.data["sets"] == [{"setName": "target_temperature"}]
    assert response.data["gets"] == [{"getName": "status"}]
    assert response.data["nests"] == [{"nestName": "Plate1"}]
    assert response.data["enter_and_exit"] == {"enterAndExitName": "plate_in"}


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


def test_synpan_mcp_cli_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["synpan-mcp", "--help"])

    assert result.exit_code == 0
    assert "Run the SynPan/CIAI MCP server" in result.stdout
