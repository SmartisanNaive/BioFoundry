# SynPan MCP Adapter

`biofoundry synpan-mcp` starts a unified stdio MCP server that exposes both the
SynPan/CIAI device driver and the SynPan third-party craft platform as tools for
Biofoundry agents. It is a client adapter: it calls existing services and does
not make Biofoundry_CLI act as a device driver or platform backend.

## Default loading

The built-in SynPan server is auto-loaded by default when `biofoundry` starts.
Disable it for one run with:

```sh
biofoundry --no-synpan-mcp
```

If you define your own `synpan` server in `.biofoundry/mcp.json` or pass one
through `--mcp-config`, that explicit config takes precedence over the built-in
default.

## Configure CIAI driver

Environment variables for the device driver (CIAI) side:

| Variable | Description |
| --- | --- |
| `SYNPAN_BASE_URL` | Default device driver URL, such as `http://127.0.0.1:9000`. |
| `SYNPAN_TOKEN` | Optional Bearer token sent as `Authorization: Bearer ...`. |
| `SYNPAN_TIMEOUT_SECONDS` | Request timeout. Defaults to `30`. |
| `SYNPAN_VERIFY_TLS` | TLS verification flag. Defaults to `true`; set `false` for local tests. |
| `SYNPAN_CA_BUNDLE` | Optional CA bundle path for HTTPS verification. |
| `SYNPAN_CLIENT_CERT` | Optional client certificate path. |
| `SYNPAN_CLIENT_KEY` | Optional client certificate key path. |

Every CIAI tool also accepts `base_url` to override `SYNPAN_BASE_URL` for one call.

## Configure third-party platform

Environment variables for the craft platform side. New `SYNPAN_PLATFORM_*`
variables are preferred; `XINGPAN_*` aliases are still supported for backward
compatibility.

| Preferred variable | Fallback alias | Description |
| --- | --- | --- |
| `SYNPAN_PLATFORM_BASE_URL` | `XINGPAN_BASE_URL` | Platform base URL, e.g. `http://host/third/party`. |
| `SYNPAN_PLATFORM_TOKEN` | `XINGPAN_TOKEN` | Token sent as `ThirdPartyToken` header. |
| `SYNPAN_PLATFORM_TIMEOUT_MS` | `XINGPAN_TIMEOUT` | Request timeout in milliseconds. Defaults to `30000`. |
| `SYNPAN_PLATFORM_VERBOSE` | `XINGPAN_VERBOSE` | Verbose logging flag. Defaults to `false`. |

## CIAI tools

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

## Platform tools

| MCP tool | Platform endpoint | Purpose |
| --- | --- | --- |
| `getWorkCellList` | `POST /thirdParty/mcp/getWorkCellList` | List work cells. |
| `getWorkCell` | `POST /thirdParty/mcp/getWorkCell` | Inspect a work cell. |
| `setWorkCell` | `POST /thirdParty/mcp/setWorkCell` | Switch active work cell. |
| `checkWorkCellAuthority` | `POST /thirdParty/mcp/checkWorkCellAuthority` | Check work cell authority. |
| `getCraftList` | `POST /thirdParty/mcp/getList` | List craft definitions. |
| `getCraft` | `POST /thirdParty/mcp/getCraft` | Inspect a craft definition. |
| `getCraftHistoryPage` | `POST /thirdParty/mcp/getCraftHistoryPage` | Paginated craft history. |
| `selectListForCanvas` | `POST /thirdParty/mcp/selectListForCanvas` | Craft canvas list. |
| `addCraft` | `POST /thirdParty/mcp/addCraft` | Create a craft. |
| `updateCraft` | `POST /thirdParty/mcp/updateCraft` | Update a craft. |
| `validateCraft` | `POST /thirdParty/mcp/validate` | Validate craft graph data. |
| `getCraftMateriel` | `POST /thirdParty/mcp/getCraftMateriel` | List craft materiel. |
| `addCraftMateriel` | `POST /thirdParty/mcp/addCraftMateriel` | Add craft materiel. |
| `deleteCraftMaterielList` | `POST /thirdParty/mcp/deleteCraftMaterielList` | Delete materiel list. |
| `getMaterielType` | `POST /thirdParty/mcp/getMaterielType` | List materiel types. |
| `getAllMaterielType` | `POST /thirdParty/mcp/getAllMaterielType` | List all materiel types for a work cell. |
| `getPositionList` | `POST /thirdParty/mcp/getPositionList` | List positions. |
| `getUnionPositionList` | `POST /thirdParty/mcp/getUnionPositionList` | List union positions. |
| `getDataTypeList` | `POST /thirdParty/mcp/getDataTypeList` | List data types. |
| `getLabelList` | `POST /thirdParty/mcp/getLabelList` | List labels for equipment. |
| `getDataObjectList` | `POST /thirdParty/data/getList` | List data objects. |
| `addDataObject` | `POST /thirdParty/data/scadaAddDataObject` | Create a data object. |
| `createOrder` | `POST /thirdParty/mcp/create` | Create an order with auto-resolved inputs. |
| `operateOrder` | `POST /thirdParty/mcp/operation` | Operate on an order. |
| `getTaskInfo` | `POST /thirdParty/mcp/getTaskInfo` | Read task info. |
| `getTaskRunLog` | `POST /thirdParty/mcp/getTaskRunLog` | Fetch task run logs. |

`createOrder` includes the same auto-resolution flow as the original Node service
for data objects and craft materiel bindings.

## Response shape

CIAI tools return:

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

Platform tools return:

```json
{
  "ok": true,
  "http_status": 200,
  "code": "200",
  "message": "Success",
  "data": {},
  "raw": {},
  "error_type": null
}
```

`raw` keeps the original service response. `data` contains `raw.data` when the
response follows the standard shape. `ok` is true for HTTP success with either no
service code or a recognized success code.

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

Create a platform order:

```json
{
  "batchNo": "batch-001",
  "craftId": "craft-001",
  "orderName": "RhlA run 1",
  "priorityLevel": 1,
  "tasks": [
    {
      "inputs": [
        {"inputName": "strain", "inputType": "data", "inputKind": "strain", "inputRest": "1"}
      ]
    }
  ]
}
```

## Notes

- The built-in implementation is native to `Biofoundry_CLI`; it does not require
  separately installed global MCP server commands.
- The previous `biofoundry xingpan-mcp` command has been merged into
  `biofoundry synpan-mcp`. The `XINGPAN_*` environment variables continue to
  work, but new configurations should use `SYNPAN_PLATFORM_*`.
