from __future__ import annotations

import os
from collections.abc import Mapping
from typing import Any, cast

import httpx

from biofoundry_cli.constant import USER_AGENT
from biofoundry_cli.synpan.models import (
    SUCCESS_CODE,
    EnterExitRequest,
    FunctionRequest,
    JsonObject,
    OperationRequest,
    SetParameter,
    SynPanResponse,
)

DEFAULT_TIMEOUT_SECONDS = 30.0


class SynPanClient:
    """HTTP client for SynPan/CIAI driver endpoints."""

    def __init__(
        self,
        *,
        base_url: str | None = None,
        token: str | None = None,
        timeout_seconds: float | None = None,
        verify_tls: bool | None = None,
        client_cert: str | None = None,
        client_key: str | None = None,
        ca_bundle: str | None = None,
        env: Mapping[str, str] | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self._env = env if env is not None else os.environ
        env_base_url = base_url if base_url is not None else self._env.get("SYNPAN_BASE_URL")
        self._base_url = _normalize_base_url(env_base_url)
        self._token = token if token is not None else self._env.get("SYNPAN_TOKEN")
        self._transport = transport
        self._configuration_error: str | None = None

        try:
            self._timeout_seconds = (
                timeout_seconds
                if timeout_seconds is not None
                else _parse_timeout(self._env.get("SYNPAN_TIMEOUT_SECONDS"))
            )
        except ValueError as exc:
            self._timeout_seconds = DEFAULT_TIMEOUT_SECONDS
            self._configuration_error = str(exc)

        if verify_tls is None:
            verify_tls = _parse_bool(self._env.get("SYNPAN_VERIFY_TLS"), default=True)
        env_ca_bundle = ca_bundle if ca_bundle is not None else self._env.get("SYNPAN_CA_BUNDLE")
        self._verify: bool | str = env_ca_bundle if env_ca_bundle else verify_tls

        env_client_cert = (
            client_cert if client_cert is not None else self._env.get("SYNPAN_CLIENT_CERT")
        )
        env_client_key = (
            client_key if client_key is not None else self._env.get("SYNPAN_CLIENT_KEY")
        )
        self._cert: str | tuple[str, str] | None
        if env_client_cert and env_client_key:
            self._cert = (env_client_cert, env_client_key)
        elif env_client_cert:
            self._cert = env_client_cert
        elif env_client_key:
            self._cert = None
            self._configuration_error = "SYNPAN_CLIENT_KEY requires SYNPAN_CLIENT_CERT."
        else:
            self._cert = None

    async def get_info(self, *, base_url: str | None = None) -> SynPanResponse:
        return await self._request("GET", "/Info", base_url=base_url)

    async def list_capabilities(self, *, base_url: str | None = None) -> SynPanResponse:
        response = await self.get_info(base_url=base_url)
        if not response.ok:
            return response

        response_data: Any | None = response.data
        if not isinstance(response_data, dict):
            return SynPanResponse.error(
                "SynPan /Info response did not contain a RegisterInfo object.",
                error_type="invalid_response",
                http_status=response.http_status,
                synpan_code=response.synpan_code,
                raw=response.raw,
            )

        capabilities = _extract_capabilities(cast(JsonObject, response_data))
        return SynPanResponse(
            ok=True,
            http_status=response.http_status,
            synpan_code=response.synpan_code,
            message=response.message,
            data=capabilities,
            raw=response.raw,
        )

    async def get_heartbeat(self, *, base_url: str | None = None) -> SynPanResponse:
        return await self._request("GET", "/HeartBeat", base_url=base_url)

    async def get_status(self, *, base_url: str | None = None) -> SynPanResponse:
        return await self._request("GET", "/Get", base_url=base_url)

    async def run_function(
        self,
        request: FunctionRequest,
        *,
        base_url: str | None = None,
    ) -> SynPanResponse:
        return await self._request(
            "POST",
            "/Function",
            json_body=request.to_synpan_payload(),
            base_url=base_url,
        )

    async def run_operation(
        self,
        request: OperationRequest,
        *,
        base_url: str | None = None,
    ) -> SynPanResponse:
        return await self._request(
            "POST",
            "/Operation",
            json_body=request.to_synpan_payload(),
            base_url=base_url,
        )

    async def set_parameters(
        self,
        parameters: list[SetParameter],
        *,
        base_url: str | None = None,
    ) -> SynPanResponse:
        payload = [parameter.to_synpan_payload() for parameter in parameters]
        return await self._request("POST", "/Set", json_body=payload, base_url=base_url)

    async def enter_and_exit(
        self,
        request: EnterExitRequest,
        *,
        base_url: str | None = None,
    ) -> SynPanResponse:
        return await self._request(
            "POST",
            "/EnterAndExit",
            json_body=request.to_synpan_payload(),
            base_url=base_url,
        )

    async def _request(
        self,
        method: str,
        endpoint: str,
        *,
        json_body: Any | None = None,
        base_url: str | None = None,
    ) -> SynPanResponse:
        if self._configuration_error is not None:
            return SynPanResponse.error(
                self._configuration_error,
                error_type="configuration",
            )

        target_base_url = _normalize_base_url(base_url) if base_url is not None else self._base_url
        if not target_base_url:
            return SynPanResponse.error(
                "SynPan base URL is not configured. Set SYNPAN_BASE_URL or pass base_url.",
                error_type="configuration",
            )

        url = f"{target_base_url}/{endpoint.lstrip('/')}"
        try:
            async with httpx.AsyncClient(
                timeout=self._timeout_seconds,
                verify=self._verify,
                cert=self._cert,
                transport=self._transport,
            ) as client:
                response = await client.request(
                    method,
                    url,
                    headers=self._headers(),
                    json=json_body,
                )
        except httpx.TimeoutException as exc:
            return SynPanResponse.error(
                f"SynPan request timed out: {exc}",
                error_type="timeout",
            )
        except httpx.RequestError as exc:
            return SynPanResponse.error(
                f"SynPan request failed: {exc}",
                error_type="network",
            )

        return _response_from_httpx(response)

    def _headers(self) -> dict[str, str]:
        headers = {
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        }
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        return headers


def _response_from_httpx(response: httpx.Response) -> SynPanResponse:
    raw: Any
    try:
        raw = response.json()
    except ValueError:
        raw = response.text
        if response.is_success:
            return SynPanResponse.error(
                "SynPan response was not valid JSON.",
                error_type="invalid_json",
                http_status=response.status_code,
                raw=raw,
            )
        return SynPanResponse.error(
            _message_from_raw(raw) or response.reason_phrase,
            error_type="http",
            http_status=response.status_code,
            raw=raw,
        )

    if not response.is_success:
        return SynPanResponse.error(
            _message_from_raw(raw) or response.reason_phrase,
            error_type="http",
            http_status=response.status_code,
            synpan_code=_synpan_code(raw),
            raw=raw,
            data=_synpan_data(raw),
        )

    synpan_code = _synpan_code(raw)
    data = _synpan_data(raw)
    message = _message_from_raw(raw) or "Success"
    ok = synpan_code is None or synpan_code == SUCCESS_CODE
    return SynPanResponse(
        ok=ok,
        http_status=response.status_code,
        synpan_code=synpan_code,
        message=message,
        data=data,
        raw=raw,
        error_type=None if ok else "synpan",
    )


def _extract_capabilities(register_info: JsonObject) -> JsonObject:
    advanced_raw = register_info.get("advancedInfo")
    advanced = cast(JsonObject, advanced_raw) if isinstance(advanced_raw, dict) else {}
    basic = register_info.get("basicInfo")
    return {
        "basic_info": basic if isinstance(basic, dict) else {},
        "functions": _list_value(advanced, "equipmentFunctions"),
        "operations": _list_value(advanced, "equipmentOperations"),
        "sets": _list_value(advanced, "equipmentSetInfos"),
        "gets": _list_value(advanced, "equipmentGetInfos"),
        "nests": _list_value(advanced, "equipmentNests"),
        "enter_and_exit": advanced.get("equipmentEnterAndExit"),
    }


def _list_value(mapping: JsonObject, key: str) -> list[Any]:
    value = mapping.get(key)
    return cast(list[Any], value) if isinstance(value, list) else []


def _message_from_raw(raw: Any) -> str | None:
    if isinstance(raw, dict):
        mapping = cast(JsonObject, raw)
        message = mapping.get("message")
        if message is not None:
            return str(message)
    if isinstance(raw, str) and raw:
        return raw
    return None


def _synpan_code(raw: Any) -> str | None:
    if isinstance(raw, dict):
        mapping = cast(JsonObject, raw)
        code = mapping.get("code")
        if code is not None:
            return str(code)
    return None


def _synpan_data(raw: Any) -> Any | None:
    if isinstance(raw, dict):
        mapping = cast(JsonObject, raw)
        if "data" in mapping:
            return mapping.get("data")
        return mapping
    return raw


def _normalize_base_url(base_url: str | None) -> str | None:
    if base_url is None:
        return None
    stripped = base_url.strip().rstrip("/")
    return stripped or None


def _parse_timeout(value: str | None) -> float:
    if value is None or not value.strip():
        return DEFAULT_TIMEOUT_SECONDS
    try:
        timeout = float(value)
    except ValueError as exc:
        raise ValueError("SYNPAN_TIMEOUT_SECONDS must be a number.") from exc
    if timeout <= 0:
        raise ValueError("SYNPAN_TIMEOUT_SECONDS must be greater than 0.")
    return timeout


def _parse_bool(value: str | None, *, default: bool) -> bool:
    if value is None or not value.strip():
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}
