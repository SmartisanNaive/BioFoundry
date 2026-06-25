from __future__ import annotations

from typing import Any

from fastmcp import FastMCP

from biofoundry_cli.synpan.client import SynPanClient
from biofoundry_cli.synpan.models import (
    EnterExitRequest,
    FunctionRequest,
    JsonObject,
    OperationRequest,
    SetParameter,
)


def create_mcp_server(client: SynPanClient | None = None) -> FastMCP:
    mcp = FastMCP(
        "SynPan CIAI",
        instructions=(
            "Tools for calling SynPan/CIAI device driver endpoints: Info, HeartBeat, "
            "Get, Function, Operation, Set, and EnterAndExit."
        ),
    )

    def active_client() -> SynPanClient:
        return client if client is not None else SynPanClient()

    async def synpan_get_info(base_url: str | None = None) -> JsonObject:
        """Get device registration metadata from the SynPan/CIAI /Info endpoint."""
        return (await active_client().get_info(base_url=base_url)).to_tool_result()

    async def synpan_list_capabilities(base_url: str | None = None) -> JsonObject:
        """List functions, operations, sets, gets, nests, and basic info from /Info."""
        return (await active_client().list_capabilities(base_url=base_url)).to_tool_result()

    async def synpan_get_heartbeat(base_url: str | None = None) -> JsonObject:
        """Read device heartbeat from the SynPan/CIAI /HeartBeat endpoint."""
        return (await active_client().get_heartbeat(base_url=base_url)).to_tool_result()

    async def synpan_get_status(base_url: str | None = None) -> JsonObject:
        """Read device status values from the SynPan/CIAI /Get endpoint."""
        return (await active_client().get_status(base_url=base_url)).to_tool_result()

    async def synpan_run_function(
        function_name: str,
        function_param: Any | None = None,
        instruction_id: str | None = None,
        labware_info: JsonObject | None = None,
        equipment_name: str | None = None,
        nest_id: str | None = None,
        user_id: str | None = None,
        task_id: str | None = None,
        base_url: str | None = None,
    ) -> JsonObject:
        """Submit a device business function through the SynPan/CIAI /Function endpoint."""
        request = FunctionRequest(
            function_name=function_name,
            function_param=function_param,
            instruction_id=instruction_id,
            labware_info=labware_info,
            equipment_name=equipment_name,
            nest_id=nest_id,
            user_id=user_id,
            task_id=task_id,
        )
        return (await active_client().run_function(request, base_url=base_url)).to_tool_result()

    async def synpan_run_operation(
        operation_name: str,
        operation_param: Any | None = None,
        base_url: str | None = None,
    ) -> JsonObject:
        """Run a device diagnostic/debug operation through the SynPan/CIAI /Operation endpoint."""
        request = OperationRequest(operation_name=operation_name, operation_param=operation_param)
        return (await active_client().run_operation(request, base_url=base_url)).to_tool_result()

    async def synpan_set_parameters(
        parameters: list[SetParameter],
        base_url: str | None = None,
    ) -> JsonObject:
        """Set device parameters through the SynPan/CIAI /Set endpoint."""
        response = await active_client().set_parameters(parameters, base_url=base_url)
        return response.to_tool_result()

    async def synpan_enter_and_exit(
        enter_or_exit_name: str,
        enter_or_exit_value: Any | None = None,
        base_url: str | None = None,
    ) -> JsonObject:
        """Run a plate/container enter-or-exit operation through /EnterAndExit."""
        request = EnterExitRequest(
            enter_or_exit_name=enter_or_exit_name,
            enter_or_exit_value=enter_or_exit_value,
        )
        return (await active_client().enter_and_exit(request, base_url=base_url)).to_tool_result()

    mcp.tool(synpan_get_info)
    mcp.tool(synpan_list_capabilities)
    mcp.tool(synpan_get_heartbeat)
    mcp.tool(synpan_get_status)
    mcp.tool(synpan_run_function)
    mcp.tool(synpan_run_operation)
    mcp.tool(synpan_set_parameters)
    mcp.tool(synpan_enter_and_exit)

    return mcp


def main() -> None:
    create_mcp_server().run(transport="stdio", show_banner=False)


if __name__ == "__main__":
    main()
