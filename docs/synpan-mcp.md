# SynPan/CIAI MCP Adapter

`biofoundry synpan-mcp` starts a stdio MCP server that exposes SynPan/CIAI device
driver endpoints as tools for Biofoundry agents. It is a client adapter: it calls
an existing device driver service and does not make Biofoundry_CLI act as a
device driver.

## Configure

Register the MCP server with the Biofoundry CLI:

```sh
biofoundry mcp add --transport stdio synpan \
  --env SYNPAN_BASE_URL=http://127.0.0.1:9000 \
  -- uv run --project /path/to/RhlA_Agent_CLI biofoundry synpan-mcp
```

Environment variables:

| Variable | Description |
| --- | --- |
| `SYNPAN_BASE_URL` | Default device driver URL, such as `http://127.0.0.1:9000`. |
| `SYNPAN_TOKEN` | Optional Bearer token sent as `Authorization: Bearer ...`. |
| `SYNPAN_TIMEOUT_SECONDS` | Request timeout. Defaults to `30`. |
| `SYNPAN_VERIFY_TLS` | TLS verification flag. Defaults to `true`; set `false` for local tests. |
| `SYNPAN_CA_BUNDLE` | Optional CA bundle path for HTTPS verification. |
| `SYNPAN_CLIENT_CERT` | Optional client certificate path. |
| `SYNPAN_CLIENT_KEY` | Optional client certificate key path. |

Every tool also accepts `base_url` to override `SYNPAN_BASE_URL` for one call.

## Tools

| MCP tool | CIAI endpoint | Purpose |
| --- | --- | --- |
| `synpan_get_info` | `GET /Info` | Read registration metadata. |
| `synpan_list_capabilities` | `GET /Info` | Extract functions, operations, sets, gets, nests, and basic info. |
| `synpan_get_heartbeat` | `GET /HeartBeat` | Read heartbeat status. |
| `synpan_get_status` | `GET /Get` | Read device status values. |
| `synpan_run_function` | `POST /Function` | Submit a device business function. |
| `synpan_run_operation` | `POST /Operation` | Run a diagnostic/debug operation. |
| `synpan_set_parameters` | `POST /Set` | Set one or more device parameters. |
| `synpan_enter_and_exit` | `POST /EnterAndExit` | Run plate/container enter-or-exit handling. |

`/FunctionSync` is intentionally not included in v1 because the CIAI Java route
builder and the standard document consistently define `/Function` as the stable
function endpoint.

## Response Shape

All tools return the same envelope:

```json
{
  "ok": true,
  "http_status": 200,
  "synpan_code": "message.common.success",
  "message": "Success",
  "data": {},
  "raw": {},
  "error_type": null
}
```

`raw` keeps the original CIAI response. `data` contains `raw.data` when the
response follows the standard `Result<T>` shape. `ok` is true for HTTP success
with either no CIAI code or `message.common.success`.

## Examples

Submit a plate reader function:

```json
{
  "function_name": "absorbance",
  "instruction_id": "rhla-read-001",
  "nest_id": "Plate1",
  "function_param": {
    "wavelength": 450,
    "readMode": "normal",
    "plateType": "96"
  }
}
```

Set target temperature:

```json
{
  "parameters": [
    {"set_name": "target_temperature", "set_value": "37"}
  ]
}
```
