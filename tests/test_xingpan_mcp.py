from __future__ import annotations

import json
from typing import Any

import httpx
import pytest
from fastmcp import Client
from typer.testing import CliRunner

from biofoundry_cli.cli import cli
from biofoundry_cli.cli.mcp import build_builtin_xingpan_mcp_config, merge_builtin_mcp_configs
from biofoundry_cli.xingpan.client import XingpanClient
from biofoundry_cli.xingpan.mcp_server import create_mcp_server


def _json_request_body(request: httpx.Request) -> Any | None:
    if not request.content:
        return None
    return json.loads(request.content.decode("utf-8"))


@pytest.mark.asyncio
async def test_xingpan_client_uses_post_and_third_party_token_header() -> None:
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

    client = XingpanClient(
        base_url="http://xingpan.local/api",
        token="token-123",
        transport=httpx.MockTransport(handler),
    )

    response = await client.post(XingpanClient.PATHS["getWorkCellList"], {})

    assert response.ok is True
    assert calls == [
        ("POST", "/api/thirdParty/mcp/getWorkCellList", "token-123", {}),
    ]


@pytest.mark.asyncio
async def test_xingpan_mcp_server_registers_and_calls_tools() -> None:
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

    client = XingpanClient(
        base_url="http://xingpan.local",
        token="token-123",
        transport=httpx.MockTransport(handler),
    )
    server = create_mcp_server(client)

    tool_names = set(await server.get_tools())
    assert {"getWorkCellList", "createOrder", "operateOrder", "getTaskInfo"} <= tool_names

    async with Client(server) as mcp_client:
        result = await mcp_client.call_tool("getWorkCellList", {})

    assert result.data["ok"] is True
    assert result.data["data"] == [{"workCellId": "wc-1", "cellName": "cell"}]


def test_builtin_xingpan_mcp_config_points_to_cli_module() -> None:
    config = build_builtin_xingpan_mcp_config()

    assert config["mcpServers"]["xingpan"]["args"] == ["-m", "biofoundry_cli.cli", "xingpan-mcp"]


def test_merge_builtin_xingpan_mcp_config_skips_existing_server() -> None:
    existing = [{"mcpServers": {"xingpan": {"command": "custom", "args": []}}}]

    merged = merge_builtin_mcp_configs(existing)

    assert merged == existing


def test_merge_builtin_xingpan_mcp_config_can_disable_default() -> None:
    merged = merge_builtin_mcp_configs([], disable_builtin_xingpan=True)

    assert merged == []


def test_xingpan_mcp_cli_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["xingpan-mcp", "--help"])

    assert result.exit_code == 0
    assert "Run the Xingpan MCP server" in result.stdout
