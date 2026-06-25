from __future__ import annotations

from typing import Any, Literal

from fastmcp import FastMCP

from biofoundry_cli.synpan.platform_client import SynPanPlatformClient
from biofoundry_cli.synpan.platform_models import JsonObject, SynPanPlatformResponse


def _dict_list(value: Any) -> list[JsonObject]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


async def _unwrap(response: SynPanPlatformResponse) -> JsonObject:
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
    client: SynPanPlatformClient,
    work_cell_id: str,
    input_payload: JsonObject,
    data_type_map: dict[str, str],
) -> JsonObject:
    input_kind = str(input_payload["inputKind"])
    data_type_id = data_type_map.get(input_kind)
    if not data_type_id:
        raise ValueError(f"未知数据类型：{input_kind}，请先调用 getDataTypeList 确认")

    existing = await client.post(
        SynPanPlatformClient.PATHS["getDataObjectList"],
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
        SynPanPlatformClient.PATHS["addDataObject"],
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
    client: SynPanPlatformClient,
    work_cell_id: str,
    input_payload: JsonObject,
) -> JsonObject:
    materials = await client.post(
        SynPanPlatformClient.PATHS["getCraftMateriel"],
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
        f'物料 "{input_name}"（类 {input_kind}）未找到，请先调用 addCraftMateriel 上料'
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


def add_platform_tools(
    mcp: FastMCP,
    client: SynPanPlatformClient | None = None,
) -> FastMCP:
    def active_client() -> SynPanPlatformClient:
        return client if client is not None else SynPanPlatformClient()

    async def getWorkCellList() -> JsonObject:
        return await _unwrap(
            await active_client().post(SynPanPlatformClient.PATHS["getWorkCellList"], {})
        )

    async def getWorkCell(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getWorkCell"],
                {"workCellId": workCellId},
            )
        )

    async def setWorkCell(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["setWorkCell"],
                {"workCellId": workCellId},
            )
        )

    async def checkWorkCellAuthority() -> JsonObject:
        return await _unwrap(
            await active_client().post(SynPanPlatformClient.PATHS["checkWorkCellAuthority"], {})
        )

    async def getCraftList(workCellId: str, userId: str | None = None) -> JsonObject:
        payload: JsonObject = {"workCellId": workCellId}
        if userId is not None:
            payload["userId"] = userId
        return await _unwrap(
            await active_client().post(SynPanPlatformClient.PATHS["getList"], payload)
        )

    async def getCraft(craftId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getCraft"], {"craftId": craftId}
            )
        )

    async def getCraftHistoryPage(craftId: str, pageNo: int, pageSize: int) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getCraftHistoryPage"],
                {"craftId": craftId, "pageNo": pageNo, "pageSize": pageSize},
            )
        )

    async def selectListForCanvas(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["selectListForCanvas"],
                {"workCellId": workCellId},
            )
        )

    async def addCraft(workCellId: str, name: str, graphData: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["addCraft"],
                {"workCellId": workCellId, "name": name, "graphData": graphData},
            )
        )

    async def updateCraft(
        craftId: str,
        workCellId: str,
        name: str,
        graphData: str,
    ) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["updateCraft"],
                {
                    "craftId": craftId,
                    "workCellId": workCellId,
                    "name": name,
                    "graphData": graphData,
                },
            )
        )

    async def validateCraft(graphData: str, cellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["validate"],
                {"graphData": graphData, "cellId": cellId},
            )
        )

    async def getCraftMateriel(
        workCellId: str,
        adscriptionMateriel: Literal[1, 2] | None = None,
    ) -> JsonObject:
        payload: JsonObject = {"workCellId": workCellId}
        if adscriptionMateriel is not None:
            payload["adscriptionMateriel"] = adscriptionMateriel
        return await _unwrap(
            await active_client().post(SynPanPlatformClient.PATHS["getCraftMateriel"], payload)
        )

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
            await active_client().post(SynPanPlatformClient.PATHS["addCraftMateriel"], payload)
        )

    async def deleteCraftMaterielList(craftMaterielIdList: list[str]) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["deleteCraftMaterielList"],
                {"craftMaterielIdList": craftMaterielIdList},
            )
        )

    async def getMaterielType() -> JsonObject:
        return await _unwrap(
            await active_client().post(SynPanPlatformClient.PATHS["getMaterielType"], {})
        )

    async def getAllMaterielType(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getAllMaterielType"],
                {"workCellId": workCellId},
            )
        )

    async def getPositionList(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getPositionList"],
                {"workCellId": workCellId},
            )
        )

    async def getUnionPositionList(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getUnionPositionList"],
                {"workCellId": workCellId},
            )
        )

    async def getDataTypeList(workCellId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getDataTypeList"],
                {"workCellId": workCellId},
            )
        )

    async def getLabelList(equipmentId: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getLabelList"],
                {"equipmentId": equipmentId},
            )
        )

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
            await active_client().post(SynPanPlatformClient.PATHS["getDataObjectList"], payload)
        )

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
            await active_client().post(SynPanPlatformClient.PATHS["addDataObject"], payload)
        )

    async def createOrder(
        batchNo: str,
        craftId: str,
        orderName: str,
        priorityLevel: Literal[1, 2, 3],
        tasks: list[dict[str, Any]],
        remark: str = "",
    ) -> JsonObject:
        platform_client = active_client()
        craft_response = await platform_client.post(
            SynPanPlatformClient.PATHS["getCraft"], {"craftId": craftId}
        )
        if not craft_response.ok or not isinstance(craft_response.data, dict):
            return await _unwrap(craft_response)

        craft = craft_response.data
        work_cell_id = str(craft.get("workCellId") or "")
        craft_inputs = _dict_list(craft.get("inputs"))
        craft_outputs = _dict_list(craft.get("outputs"))

        data_types_response = await platform_client.post(
            SynPanPlatformClient.PATHS["getDataTypeList"],
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
                            platform_client,
                            work_cell_id,
                            filled,
                            data_type_map,
                        )
                    elif input_type == "material":
                        resolved = await _resolve_material_input(
                            platform_client, work_cell_id, filled
                        )
                    else:
                        resolved = filled
                    resolved_inputs.append(resolved)

                outputs_value = _dict_list(task.get("outputs")) or None
                resolved_outputs = _fill_outputs(outputs_value, craft_outputs)
                resolved_tasks.append(
                    {**task, "inputs": resolved_inputs, "outputs": resolved_outputs}
                )
        except ValueError as exc:
            return SynPanPlatformResponse.error(str(exc), error_type="validation").to_tool_result()

        payload = {
            "batchNo": batchNo,
            "craftId": craftId,
            "orderName": orderName,
            "priorityLevel": priorityLevel,
            "remark": remark,
            "tasks": resolved_tasks,
        }
        return await _unwrap(
            await platform_client.post(SynPanPlatformClient.PATHS["create"], payload)
        )

    async def operateOrder(batchNo: str, operation: Literal[1, 2, 3]) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["operation"],
                {"batchNo": batchNo, "operation": operation},
            )
        )

    async def getTaskInfo(batchNo: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getTaskInfo"],
                {"batchNo": batchNo},
            )
        )

    async def getTaskRunLog(batchNo: str) -> JsonObject:
        return await _unwrap(
            await active_client().post(
                SynPanPlatformClient.PATHS["getTaskRunLog"],
                {"batchNo": batchNo},
            )
        )

    mcp.tool(getWorkCellList)
    mcp.tool(getWorkCell)
    mcp.tool(setWorkCell)
    mcp.tool(checkWorkCellAuthority)
    mcp.tool(getCraftList)
    mcp.tool(getCraft)
    mcp.tool(getCraftHistoryPage)
    mcp.tool(selectListForCanvas)
    mcp.tool(addCraft)
    mcp.tool(updateCraft)
    mcp.tool(validateCraft)
    mcp.tool(getCraftMateriel)
    mcp.tool(addCraftMateriel)
    mcp.tool(deleteCraftMaterielList)
    mcp.tool(getMaterielType)
    mcp.tool(getAllMaterielType)
    mcp.tool(getPositionList)
    mcp.tool(getUnionPositionList)
    mcp.tool(getDataTypeList)
    mcp.tool(getLabelList)
    mcp.tool(getDataObjectList)
    mcp.tool(addDataObject)
    mcp.tool(createOrder)
    mcp.tool(operateOrder)
    mcp.tool(getTaskInfo)
    mcp.tool(getTaskRunLog)

    return mcp
