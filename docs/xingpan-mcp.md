# Xingpan MCP Service

`biofoundry xingpan-mcp` starts a stdio MCP server that exposes Xingpan third-party endpoints as tools for Biofoundry agents.

## Default loading

Unlike manually registered MCP servers, the built-in Xingpan server is auto-loaded by default when `biofoundry` starts.

Disable it for one run with:

```sh
biofoundry --no-xingpan-mcp
```

If you define your own `xingpan` server in `.biofoundry/mcp.json` or pass one through `--mcp-config`, that explicit config takes precedence over the built-in default.

## Configure

Set environment variables before startup:

```sh
export XINGPAN_BASE_URL="http://host/third/party"
export XINGPAN_TOKEN="your-token"
# optional
export XINGPAN_TIMEOUT="30000"
export XINGPAN_VERBOSE="true"
```

## Main tool groups

- work cell: list, inspect, switch, and authority check
- craft: list, inspect, validate, create, and update
- materiel: list, add, delete, and inspect positions/types
- data: list and create data objects
- order: create, operate, inspect task info, and fetch run logs

## Notes

- The built-in implementation is native to `Biofoundry_CLI`; it does not require a separately installed global `xingpan-mcp-server` command.
- `create_order` includes the same auto-resolution flow as the original Node service for data objects and craft materiel bindings.
