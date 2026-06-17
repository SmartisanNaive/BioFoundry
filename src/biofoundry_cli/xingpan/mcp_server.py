from __future__ import annotations

from typing import Any, Literal

from fastmcp import FastMCP

from biofoundry_cli.xingpan.client import XingpanClient
from biofoundry_cli.xingpan.models import JsonObject, XingpanResponse


def _dict_list(value: Any) -> list[JsonObject]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


async def _unwrap(response: XingpanResponse) -> JsonObject:
    return response.to_tool_result()


def _fill_from_craft_def(
    input_payload: JsonObject,
    craft_input_def: JsonObject | None,
) -> JsonObject:
    craft_input_def = craft_input_def or {}
    return {
        **input_payload,
        "inputRest": input_payload.get("inputRest") or craft_input_def.get("inputRest") or "1",
        "inputObj": input_payload.get("inputObj") if "inputObj" in input_payload else None,
    }


async def _resolve_data_input(
    client: XingpanClient,
    work_cell_id: str,
    input_payload: JsonObject,
    data_type_map: dict[str, str],
) -> JsonObject:
    input_kind = str(input_payload["inputKind"])
    data_type_id = data_type_map.get(input_kind)
    if not data_type_id:
        raise ValueError(f"未知数据类型：{input_kind}，请先调用 getDataTypeList 确认")

    existing = await client.post(
        XingpanClient.PATHS["getDataObjectList"],
        {"workCellId": work_cell_id, "name": input_payload["inputName"]},
    )
    if existing.ok:
        for item in _dict_list(existing.data):
            if item.get("name") == input_payload["inputName"]:
                return {
                    **input_payload,
                    "inputObjId": item.get("dataObjectId", ""),
                    "inputObjName": item.get("name", ""),
                }

    created = await client.post(
        XingpanClient.PATHS["addDataObject"],
        {
            "workCellId": work_cell_id,
            "name": input_payload["inputName"],
            "dataTypeId": data_type_id,
        },
    )
    if not created.ok:
        raise ValueError(created.message)

    new_id = (
        created.data
        if isinstance(created.data, str)
        else (created.data or {}).get("dataObjectId", "")
    )
    return {
        **input_payload,
        "inputObjId": new_id,
        "inputObjName": input_payload["inputName"],
    }


async def _resolve_material_input(
    client: XingpanClient,
    work_cell_id: str,
    input_payload: JsonObject,
) -> JsonObject:
    materials = await client.post(
        XingpanClient.PATHS["getCraftMateriel"],
        {"workCellId": work_cell_id},
    )
    if materials.ok:
        input_kind = input_payload["inputKind"]
        for item in _dict_list(materials.data):
            materiel_class = item.get("materielClassName") or item.get("materielClass")
            if materiel_class == input_kind:
                return {
                    **input_payload,
                    "inputObjId": item.get("craftMaterielId", ""),
                    "inputObjName": item.get("materielName", ""),
                }

    input_name = input_payload["inputName"]
    input_kind = input_payload["inputKind"]
    raise ValueError(
        f"物料 \"{input_name}\"（类 {input_kind}）未找到，请先调用 addCraftMateriel 上料"
    )


def _fill_outputs(
    task_outputs: list[JsonObject] | None,
    craft_outputs: list[JsonObject],
) -> list[JsonObject]:
    if task_outputs:
        return [
            {
                **output,
                "outputDefineName": output.get("outputDefineName") or output["outputName"],
                "outputRest": output.get("outputRest") or "",
            }
            for output in task_outputs
        ]

    return [
        {
            "outputType": output.get("outputType"),
            "outputTypeName": output.get("outputTypeName"),
            "outputName": output.get("outputName"),
            "outputDefineName": output.get("outputDefineName") or output.get("outputName"),
            "outputKind": output.get("outputKind"),
            "outputRest": output.get("outputRest") or "",
        }
        for output in craft_outputs
    ]


def create_mcp_server(client: XingpanClient | None = None) -> FastMCP:
    mcp = FastMCP(
        "Xingpan",
        instructions=(
            "Tools for calling Xingpan third-party endpoints for workcells, craft, "
            "materiel, data, and orders."
        ),
    )

    def active_client() -> XingpanClient:
        return client if client is not None else XingpanClient()

    @mcp.tool
    async def getWorkCellList() -> JsonObject:
        return await _unwrap(await active_client().post(XingpanClient.PATHS["getWorkCellList"], {}))

    @mcp.tool
    async def getWorkCell(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getWorkCell"],
                {"workCellId": workCellId},
            )
        )

    @mcp.tool
    async def setWorkCell(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["setWorkCell"],
                {"workCellId": workCellId},
            )
        )

    @mcp.tool
    async def checkWorkCellAuthority() -> JsonObject:
        return await _unwrap(
            await active_client().post(XingpanClient.PATHS["checkWorkCellAuthority"], {})
        )

    @mcp.tool
    async def getCraftList(workCellId: str, userId: str | None = None) -> JsonObject:
        payload: JsonObject = {"workCellId": workCellId}
        if userId is not None:
            payload["userId"] = userId
        return await _unwrap(await active_client().post(XingpanClient.PATHS["getList"], payload))

    @mcp.tool
    async def getCraft(craftId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(XingpanClient.PATHS["getCraft"], {"craftId": craftId})
        )

    @mcp.tool
    async def getCraftHistoryPage(craftId: str, pageNo: int, pageSize: int) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getCraftHistoryPage"],
                {"craftId": craftId, "pageNo": pageNo, "pageSize": pageSize},
            )
        )

    @mcp.tool
    async def selectListForCanvas(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["selectListForCanvas"],
                {"workCellId": workCellId},
            )
        )

    @mcp.tool
    async def addCraft(workCellId: str, name: str, graphData: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["addCraft"],
                {"workCellId": workCellId, "name": name, "graphData": graphData},
            )
        )

    @mcp.tool
    async def updateCraft(
        craftId: str,
        workCellId: str,
        name: str,
        graphData: str,
    ) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["updateCraft"],
                {
                    "craftId": craftId,
                    "workCellId": workCellId,
                    "name": name,
                    "graphData": graphData,
                },
            )
        )

    @mcp.tool
    async def validateCraft(graphData: str, cellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["validate"],
                {"graphData": graphData, "cellId": cellId},
            )
        )

    @mcp.tool
    async def getCraftMateriel(
        workCellId: str,
        adscriptionMateriel: Literal[1, 2] | None = None,
    ) -> JsonObject:
        payload: JsonObject = {"workCellId": workCellId}
        if adscriptionMateriel is not None:
            payload["adscriptionMateriel"] = adscriptionMateriel
        return await _unwrap(
            await active_client().post(XingpanClient.PATHS["getCraftMateriel"], payload)
        )

    @mcp.tool
    async def addCraftMateriel(
        workCellId: str,
        materielName: str,
        materielClassName: str,
        positionId: str,
        posture: str,
        adscriptionMateriel: Literal[1, 2],
        materielClassAdscription: Literal[1, 2],
        serialNumber: str | None = None,
        userId: str | None = None,
    ) -> JsonObject:
        payload: JsonObject = {
            "workCellId": workCellId,
            "materielName": materielName,
            "materielClassName": materielClassName,
            "positionId": positionId,
            "posture": posture,
            "adscriptionMateriel": adscriptionMateriel,
            "materielClassAdscription": materielClassAdscription,
        }
        if serialNumber is not None:
            payload["serialNumber"] = serialNumber
        if userId is not None:
            payload["userId"] = userId
        return await _unwrap(
            await active_client().post(XingpanClient.PATHS["addCraftMateriel"], payload)
        )

    @mcp.tool
    async def deleteCraftMaterielList(craftMaterielIdList: list[str]) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["deleteCraftMaterielList"],
                {"craftMaterielIdList": craftMaterielIdList},
            )
        )

    @mcp.tool
    async def getMaterielType() -> JsonObject:
        return await _unwrap(await active_client().post(XingpanClient.PATHS["getMaterielType"], {}))

    @mcp.tool
    async def getAllMaterielType(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getAllMaterielType"],
                {"workCellId": workCellId},
            )
        )

    @mcp.tool
    async def getPositionList(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getPositionList"],
                {"workCellId": workCellId},
            )
        )

    @mcp.tool
    async def getUnionPositionList(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getUnionPositionList"],
                {"workCellId": workCellId},
            )
        )

    @mcp.tool
    async def getDataTypeList(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getDataTypeList"],
                {"workCellId": workCellId},
            )
        )

    @mcp.tool
    async def getLabelList(equipmentId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getLabelList"],
                {"equipmentId": equipmentId},
            )
        )

    @mcp.tool
    async def getDataObjectList(
        workCellId: str,
        name: str | None = None,
        userId: str | None = None,
    ) -> JsonObject:
        payload: JsonObject = {"workCellId": workCellId}
        if name is not None:
            payload["name"] = name
        if userId is not None:
            payload["userId"] = userId
        return await _unwrap(
            await active_client().post(XingpanClient.PATHS["getDataObjectList"], payload)
        )

    @mcp.tool
    async def addDataObject(
        workCellId: str,
        name: str,
        dataTypeId: str,
        objectValue: str | None = None,
        childElementTypeId: str | None = None,
        arrayShape: str | None = None,
        remark: str | None = None,
        userId: str | None = None,
    ) -> JsonObject:
        payload: JsonObject = {
            "workCellId": workCellId,
            "name": name,
            "dataTypeId": dataTypeId,
        }
        if objectValue is not None:
            payload["objectValue"] = objectValue
        if childElementTypeId is not None:
            payload["childElementTypeId"] = childElementTypeId
        if arrayShape is not None:
            payload["arrayShape"] = arrayShape
        if remark is not None:
            payload["remark"] = remark
        if userId is not None:
            payload["userId"] = userId
        return await _unwrap(
            await active_client().post(XingpanClient.PATHS["addDataObject"], payload)
        )

    @mcp.tool
    async def createOrder(
        batchNo: str,
        craftId: str,
        orderName: str,
        priorityLevel: Literal[1, 2, 3],
        tasks: list[dict[str, Any]],
        remark: str = "",
    ) -> JsonObject:
        client = active_client()
        craft_response = await client.post(XingpanClient.PATHS["getCraft"], {"craftId": craftId})
        if not craft_response.ok or not isinstance(craft_response.data, dict):
            return await _unwrap(craft_response)

        craft = craft_response.data
        work_cell_id = str(craft.get("workCellId") or "")
        craft_inputs = _dict_list(craft.get("inputs"))
        craft_outputs = _dict_list(craft.get("outputs"))

        data_types_response = await client.post(
            XingpanClient.PATHS["getDataTypeList"],
            {"workCellId": work_cell_id},
        )
        if not data_types_response.ok:
            return await _unwrap(data_types_response)

        data_type_map = {
            str(item.get("typeName")): str(item.get("id"))
            for item in _dict_list(data_types_response.data)
            if item.get("typeName") is not None and item.get("id") is not None
        }

        try:
            resolved_tasks: list[JsonObject] = []
            for task in tasks:
                inputs = _dict_list(task.get("inputs"))
                resolved_inputs: list[JsonObject] = []
                for input_payload in inputs:
                    craft_input_def = next(
                        (
                            item
                            for item in craft_inputs
                            if item.get("inputName") == input_payload.get("inputName")
                        ),
                        None,
                    )
                    filled = _fill_from_craft_def(input_payload, craft_input_def)
                    input_type = str(filled.get("inputType"))
                    if input_type == "data":
                        resolved = await _resolve_data_input(
                            client,
                            work_cell_id,
                            filled,
                            data_type_map,
                        )
                    elif input_type == "material":
                        resolved = await _resolve_material_input(client, work_cell_id, filled)
                    else:
                        resolved = filled
                    resolved_inputs.append(resolved)

                outputs_value = _dict_list(task.get("outputs")) or None
                resolved_outputs = _fill_outputs(outputs_value, craft_outputs)
                resolved_tasks.append(
                    {**task, "inputs": resolved_inputs, "outputs": resolved_outputs}
                )
        except ValueError as exc:
            return XingpanResponse.error(str(exc), error_type="validation").to_tool_result()

        payload = {
            "batchNo": batchNo,
            "craftId": craftId,
            "orderName": orderName,
            "priorityLevel": priorityLevel,
            "remark": remark,
            "tasks": resolved_tasks,
        }
        return await _unwrap(await client.post(XingpanClient.PATHS["create"], payload))

    @mcp.tool
    async def operateOrder(batchNo: str, operation: Literal[1, 2, 3]) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["operation"],
                {"batchNo": batchNo, "operation": operation},
            )
        )

    @mcp.tool
    async def getTaskInfo(batchNo: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getTaskInfo"],
                {"batchNo": batchNo},
            )
        )

    @mcp.tool
    async def getTaskRunLog(batchNo: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                XingpanClient.PATHS["getTaskRunLog"],
                {"batchNo": batchNo},
            )
        )

    return mcp


def main() -> None:
    create_mcp_server().run(transport="stdio", show_banner=False)


if __name__ == "__main__":
    main()
