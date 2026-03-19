# Biofoundry_CLI Tools

## Guidelines

- Except for `Task` tool, tools should not refer to any types in `biofoundry_cli/wire/`. When importing things like `ToolReturnValue`, `DisplayBlock`, import from `biofoundry_llm.tooling`.
