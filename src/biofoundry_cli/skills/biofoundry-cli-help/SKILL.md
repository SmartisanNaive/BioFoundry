---
name: biofoundry-cli-help
description: Answer Biofoundry_CLI usage, configuration, and troubleshooting questions. Use when user asks about Biofoundry_CLI installation, setup, configuration, slash commands, keyboard shortcuts, MCP integration, providers, environment variables, how something works internally, or any questions about Biofoundry_CLI itself.
---

# Biofoundry_CLI Help

Help users with Biofoundry_CLI questions by consulting documentation and source code.

## Strategy

1. **Prefer local source** for product-specific behavior, flags, and internal architecture.
2. **Read the current project files first** when in the Biofoundry_CLI repository or when the user imports `biofoundry_cli` as a library.
3. **Use external docs only when needed** and treat outdated branding or URLs as historical references, not the source of truth.

## Source of Truth

- CLI package: `biofoundry_cli`
- Primary command: `biofoundry`
- Share directory: `.biofoundry` in the project root
- Config file: `.biofoundry/config.toml` in the project root

When to read source:

- In the Biofoundry_CLI project directory
- User is importing `biofoundry_cli` as a library in their project
- Question is about internals, behavior, prompts, tools, ACP, wire, or shell UI
