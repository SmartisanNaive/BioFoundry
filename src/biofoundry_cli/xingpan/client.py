from __future__ import annotations

import os
from collections.abc import Mapping
from typing import Any, cast

import httpx

from biofoundry_cli.constant import USER_AGENT
from biofoundry_cli.xingpan.models import JsonObject, XingpanResponse

DEFAULT_TIMEOUT_MS = 30000.0


class XingpanClient:
    PATHS = {
        "addCraft": "/thirdParty/mcp/addCraft",
        "updateCraft": "/thirdParty/mcp/updateCraft",
        "getList": "/thirdParty/mcp/getList",
        "getCraft": "/thirdParty/mcp/getCraft",
        "selectListForCanvas": "/thirdParty/mcp/selectListForCanvas",
        "validate": "/thirdParty/mcp/validate",
        "getCraftHistoryPage": "/thirdParty/mcp/getCraftHistoryPage",
        "checkWorkCellAuthority": "/thirdParty/mcp/checkWorkCellAuthority",
        "getAllMaterielType": "/thirdParty/mcp/getAllMaterielType",
        "getDataTypeList": "/thirdParty/mcp/getDataTypeList",
        "getLabelList": "/thirdParty/mcp/getLabelList",
        "getDataObjectList": "/thirdParty/data/getList",
        "addDataObject": "/thirdParty/data/scadaAddDataObject",
        "addCraftMateriel": "/thirdParty/mcp/addCraftMateriel",
        "deleteCraftMaterielList": "/thirdParty/mcp/deleteCraftMaterielList",
        "getCraftMateriel": "/thirdParty/mcp/getCraftMateriel",
        "getMaterielType": "/thirdParty/mcp/getMaterielType",
        "getPositionList": "/thirdParty/mcp/getPositionList",
        "getUnionPositionList": "/thirdParty/mcp/getUnionPositionList",
        "getWorkCell": "/thirdParty/mcp/getWorkCell",
        "getWorkCellList": "/thirdParty/mcp/getWorkCellList",
        "setWorkCell": "/thirdParty/mcp/setWorkCell",
        "create": "/thirdParty/mcp/create",
        "operation": "/thirdParty/mcp/operation",
        "getTaskInfo": "/thirdParty/mcp/getTaskInfo",
        "getTaskRunLog": "/thirdParty/mcp/getTaskRunLog",
    }

    def __init__(
        self,
        *,
        base_url: str | None = None,
        token: str | None = None,
        timeout_ms: float | None = None,
        env: Mapping[str, str] | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self._env = env if env is not None else os.environ
        env_base_url = base_url if base_url is not None else self._env.get("XINGPAN_BASE_URL")
        self._base_url = _normalize_base_url(env_base_url)
        self._token = token if token is not None else self._env.get("XINGPAN_TOKEN")
        self._transport = transport
        self._configuration_error: str | None = None
        try:
            self._timeout_ms = (
                timeout_ms
                if timeout_ms is not None
                else _parse_timeout(self._env.get("XINGPAN_TIMEOUT"))
            )
        except ValueError as exc:
            self._timeout_ms = DEFAULT_TIMEOUT_MS
            self._configuration_error = str(exc)
        self._verbose = _parse_bool(self._env.get("XINGPAN_VERBOSE"), default=False)

    async def post(
        self,
        path: str,
        body: Any | None = None,
        *,
        base_url: str | None = None,
    ) -> XingpanResponse:
        if self._configuration_error is not None:
            return XingpanResponse.error(self._configuration_error, error_type="configuration")

        target_base_url = _normalize_base_url(base_url) if base_url is not None else self._base_url
        if not target_base_url:
            return XingpanResponse.error(
                "Xingpan base URL is not configured. Set XINGPAN_BASE_URL or pass base_url.",
                error_type="configuration",
            )
        if not self._token:
            return XingpanResponse.error(
                "Xingpan token is not configured. Set XINGPAN_TOKEN.",
                error_type="configuration",
            )

        url = target_base_url + path
        try:
            async with httpx.AsyncClient(
                timeout=self._timeout_ms / 1000.0,
                transport=self._transport,
            ) as client:
                response = await client.post(
                    url,
                    headers=self._headers(),
                    json=body if body is not None else {},
                )
        except httpx.TimeoutException as exc:
            return XingpanResponse.error(f"Xingpan request timed out: {exc}", error_type="timeout")
        except httpx.RequestError as exc:
            return XingpanResponse.error(f"Xingpan request failed: {exc}", error_type="network")

        return _response_from_httpx(response)

    def _headers(self) -> dict[str, str]:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": USER_AGENT,
            "ThirdPartyToken": self._token or "",
        }
        return headers


def _response_from_httpx(response: httpx.Response) -> XingpanResponse:
    raw: Any
    try:
        raw = response.json()
    except ValueError:
        raw = response.text
        if response.is_success:
            return XingpanResponse.error(
                "Xingpan response was not valid JSON.",
                error_type="invalid_json",
                http_status=response.status_code,
                raw=raw,
            )
        return XingpanResponse.error(
            _message_from_raw(raw) or response.reason_phrase,
            error_type="http",
            http_status=response.status_code,
            raw=raw,
        )

    mapping = cast(JsonObject, raw) if isinstance(raw, dict) else {}
    code = _code_from_raw(raw)
    data = mapping.get("data") if isinstance(raw, dict) and "data" in mapping else raw
    message = _message_from_raw(raw) or "Success"

    if not response.is_success:
        return XingpanResponse.error(
            message,
            error_type="http",
            http_status=response.status_code,
            code=code,
            raw=raw,
            data=data,
        )

    if isinstance(mapping.get("code"), int) and mapping["code"] not in {0, 200}:
        return XingpanResponse.error(
            message,
            error_type="biz",
            http_status=response.status_code,
            code=code,
            raw=raw,
            data=data,
        )
    if mapping.get("success") is False:
        return XingpanResponse.error(
            message,
            error_type="biz",
            http_status=response.status_code,
            code=code,
            raw=raw,
            data=data,
        )

    return XingpanResponse(
        ok=True,
        http_status=response.status_code,
        code=code,
        message=message,
        data=data,
        raw=raw,
    )


def _normalize_base_url(base_url: str | None) -> str | None:
    if base_url is None:
        return None
    stripped = base_url.strip().rstrip("/")
    return stripped or None


def _parse_timeout(value: str | None) -> float:
    if value is None or not value.strip():
        return DEFAULT_TIMEOUT_MS
    try:
        timeout = float(value)
    except ValueError as exc:
        raise ValueError("XINGPAN_TIMEOUT must be a number.") from exc
    if timeout <= 0:
        raise ValueError("XINGPAN_TIMEOUT must be greater than 0.")
    return timeout


def _parse_bool(value: str | None, *, default: bool) -> bool:
    if value is None or not value.strip():
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _message_from_raw(raw: Any) -> str | None:
    if isinstance(raw, dict):
        mapping = cast(JsonObject, raw)
        message = mapping.get("message")
        if message is not None:
            return str(message)
    if isinstance(raw, str) and raw:
        return raw
    return None


def _code_from_raw(raw: Any) -> str | None:
    if isinstance(raw, dict):
        mapping = cast(JsonObject, raw)
        code = mapping.get("code")
        if code is not None:
            return str(code)
    return None
