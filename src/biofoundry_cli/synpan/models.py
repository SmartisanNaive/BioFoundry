from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

SUCCESS_CODE = "message.common.success"

type JsonObject = dict[str, Any]


class SynPanResponse(BaseModel):
    ok: bool
    http_status: int | None = None
    synpan_code: str | None = None
    message: str
    data: Any | None = None
    raw: Any | None = None
    error_type: str | None = None

    def to_tool_result(self) -> JsonObject:
        return self.model_dump(mode="json")

    @classmethod
    def error(
        cls,
        message: str,
        *,
        error_type: str,
        http_status: int | None = None,
        synpan_code: str | None = None,
        raw: Any | None = None,
        data: Any | None = None,
    ) -> SynPanResponse:
        return cls(
            ok=False,
            http_status=http_status,
            synpan_code=synpan_code,
            message=message,
            data=data,
            raw=raw,
            error_type=error_type,
        )


class FunctionRequest(BaseModel):
    function_name: str = Field(min_length=1)
    function_param: Any | None = None
    instruction_id: str | None = None
    labware_info: JsonObject | None = None
    equipment_name: str | None = None
    nest_id: str | None = None
    user_id: str | None = None
    task_id: str | None = None

    def to_synpan_payload(self) -> JsonObject:
        payload: JsonObject = {"functionName": self.function_name}
        _put_if_present(payload, "functionParam", self.function_param)
        _put_if_present(payload, "instructionId", self.instruction_id)
        _put_if_present(payload, "labwareInfo", self.labware_info)
        _put_if_present(payload, "equipmentName", self.equipment_name)
        _put_if_present(payload, "nestId", self.nest_id)
        _put_if_present(payload, "userId", self.user_id)
        _put_if_present(payload, "taskId", self.task_id)
        return payload


class OperationRequest(BaseModel):
    operation_name: str = Field(min_length=1)
    operation_param: Any | None = None

    def to_synpan_payload(self) -> JsonObject:
        payload: JsonObject = {"operationName": self.operation_name}
        _put_if_present(payload, "operationParam", self.operation_param)
        return payload


class SetParameter(BaseModel):
    set_name: str = Field(min_length=1)
    set_value: Any

    def to_synpan_payload(self) -> JsonObject:
        return {"setName": self.set_name, "setValue": self.set_value}


class EnterExitRequest(BaseModel):
    enter_or_exit_name: str = Field(min_length=1)
    enter_or_exit_value: Any | None = None

    def to_synpan_payload(self) -> JsonObject:
        payload: JsonObject = {"enterOrExitName": self.enter_or_exit_name}
        _put_if_present(payload, "enterOrExitValue", self.enter_or_exit_value)
        return payload


HeartbeatStatus = Literal[
    "normal",
    "driver_abnormal",
    "driver_timeout",
    "equipment_abnormal",
    "equipment_error",
    "equipment_timeout",
    "monitoring",
]


def _put_if_present(payload: JsonObject, key: str, value: Any | None) -> None:
    if value is not None:
        payload[key] = value
