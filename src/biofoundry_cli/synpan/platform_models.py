from __future__ import annotations

from typing import Any

from pydantic import BaseModel

type JsonObject = dict[str, Any]


class SynPanPlatformResponse(BaseModel):
    ok: bool
    http_status: int | None = None
    code: str | None = None
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
        code: str | None = None,
        raw: Any | None = None,
        data: Any | None = None,
    ) -> SynPanPlatformResponse:
        return cls(
            ok=False,
            http_status=http_status,
            code=code,
            message=message,
            data=data,
            raw=raw,
            error_type=error_type,
        )
