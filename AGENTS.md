# Biofoundry_CLI

## Quick commands (use uv)

- `make prepare` (sync deps for all workspace packages and install git hooks)
- `make format`
- `make check`
- `make test`
- `make ai-test`
- `make build` / `make build-bin`

If running tools directly, use `uv run ...`.

## Project overview

Biofoundry_CLI is a Python CLI agent for software engineering workflows. It supports an interactive
shell UI, ACP server mode for IDE integrations, and MCP tool loading.

## Tech stack

- Python 3.12+ (tooling configured for 3.14)
- CLI framework: Typer
- Async runtime: asyncio
- LLM framework: biofoundry_llm
- MCP integration: fastmcp
- Logging: loguru
- Package management/build: uv + uv_build; PyInstaller for binaries
- Tests: pytest + pytest-asyncio; lint/format: ruff; types: pyright + ty

## Architecture overview

- **CLI entry**: `src/biofoundry_cli/cli.py` (Typer) parses flags (UI mode, agent spec, config, MCP)
  and routes into `BiofoundryCLI` in `src/biofoundry_cli/app.py`.
- **App/runtime setup**: `BiofoundryCLI.create` loads config (`src/biofoundry_cli/config.py`), chooses a
  model/provider (`src/biofoundry_cli/llm.py`), builds a `Runtime` (`src/biofoundry_cli/soul/agent.py`),
  loads an agent spec, restores `Context`, then constructs `BiofoundrySoul`.
- **Agent specs**: YAML under `src/biofoundry_cli/agents/` loaded by `src/biofoundry_cli/agentspec.py`.
  Specs can `extend` base agents, select tools by import path, and define fixed subagents.
  System prompts live alongside specs; builtin args include `BIOFOUNDRY_NOW`,
  `BIOFOUNDRY_WORK_DIR`, `BIOFOUNDRY_WORK_DIR_LS`, `BIOFOUNDRY_AGENTS_MD`,
  `BIOFOUNDRY_SKILLS`, and `BIOFOUNDRY_KNOWLEDGE` (this file is injected via `BIOFOUNDRY_AGENTS_MD`).
- **Embedded knowledge/skills**: `src/biofoundry_cli/resources.py` resolves bundled resource roots
  from the installed package location instead of the current working directory. It exposes
  built-in skills from `src/biofoundry_cli/skills/` plus project-bundled domain skills and
  papers under `Knowledge/`, so agents can still discover and read them when running in any
  workspace.
- **Tooling**: `src/biofoundry_cli/soul/toolset.py` loads tools by import path, injects dependencies,
  and runs tool calls. Built-in tools live in `src/biofoundry_cli/tools/` (shell, file, web, todo,
  multiagent, dmail, think). MCP tools are loaded via `fastmcp`; CLI management is in
  `src/biofoundry_cli/mcp.py` and stored in the share dir.
- **Subagents**: `LaborMarket` in `src/biofoundry_cli/soul/agent.py` manages fixed and dynamic
  subagents. The Task tool (`src/biofoundry_cli/tools/multiagent/`) spawns them.
- **Core loop**: `src/biofoundry_cli/soul/biofoundrysoul.py` is the main agent loop. It accepts user input,
  handles slash commands (`src/biofoundry_cli/soul/slash.py`), appends to `Context`
  (`src/biofoundry_cli/soul/context.py`), calls the LLM (`biofoundry_llm`), runs tools, and performs compaction
  (`src/biofoundry_cli/soul/compaction.py`) when needed.
- **Approvals**: `src/biofoundry_cli/soul/approval.py` mediates user approvals for tool actions; the
  soul forwards approval requests over `Wire` for UI handling.
- **UI/Wire**: `src/biofoundry_cli/soul/run_soul` connects `BiofoundrySoul` to a `Wire`
  (`src/biofoundry_cli/wire/`) so UI loops can stream events. UIs live in `src/biofoundry_cli/ui/`
  (shell/print/acp/wire).
- **Shell UI**: `src/biofoundry_cli/ui/shell/` handles interactive TUI input, shell command mode,
  and slash command autocomplete; it is the default interactive experience.
- **Slash commands**: Soul-level commands live in `src/biofoundry_cli/soul/slash.py`; shell-level
  commands live in `src/biofoundry_cli/ui/shell/slash.py`. The shell UI exposes both and dispatches
  based on the registry. Standard skills register `/skill:<skill-name>` and load `SKILL.md`
  as a user prompt; flow skills register `/flow:<skill-name>` and execute the embedded flow.

## Major modules and interfaces

- `src/biofoundry_cli/app.py`: `BiofoundryCLI.create(...)` and `BiofoundryCLI.run(...)` are the main programmatic
  entrypoints; this is what UI layers use.
- `src/biofoundry_cli/soul/agent.py`: `Runtime` (config, session, builtins), `Agent` (system prompt +
  toolset), and `LaborMarket` (subagent registry).
- `src/biofoundry_cli/soul/biofoundrysoul.py`: `BiofoundrySoul.run(...)` is the loop boundary; it emits Wire
  messages and executes tools via `BiofoundryToolset`.
- `src/biofoundry_cli/soul/context.py`: conversation history + checkpoints; used by DMail for
  checkpointed replies.
- `src/biofoundry_cli/soul/toolset.py`: load tools, run tool calls, bridge to MCP tools.
- `src/biofoundry_cli/ui/*`: shell/print/acp frontends; they consume `Wire` messages.
- `src/biofoundry_cli/wire/*`: event types and transport used between soul and UI.

## Repo map

- `src/biofoundry_cli/agents/`: built-in agent YAML specs and prompts
- `src/biofoundry_cli/resources.py`: packaged resource path resolution for embedded skills and knowledge
- `src/biofoundry_cli/prompts/`: shared prompt templates
- `src/biofoundry_cli/soul/`: core runtime/loop, context, compaction, approvals
- `src/biofoundry_cli/tools/`: built-in tools
- `src/biofoundry_cli/ui/`: UI frontends (shell/print/acp/wire)
- `src/biofoundry_cli/acp/`: ACP server components
- `Knowledge/`: project-bundled domain knowledge, including `biofoundry-skills/` and `Paper/`
- `packages/biofoundry_llm/`, `packages/biofoundry_os/`: workspace deps
  + `biofoundry_llm` is the LLM abstraction layer for modern AI agent applications.
    It unifies message structures, asynchronous tool orchestration, and pluggable
    chat providers so you can build agents with ease and avoid vendor lock-in.
  + `biofoundry_os` is the operating-system abstraction layer for local and remote
    agent execution over local subprocesses and SSH.
- `tests/`, `tests_ai/`: test suites
- `klips`: Biofoundry_CLI Improvement Proposals

## Conventions and quality

- Python >=3.12 (ty config uses 3.14); line length 100.
- Ruff handles lint + format (rules: E, F, UP, B, SIM, I); pyright + ty for type checks.
- Tests use pytest + pytest-asyncio; files are `tests/test_*.py`.
- CLI entry points: `biofoundry` -> `src/biofoundry_cli/cli.py`.
- User config: `.biofoundry/config.toml` in the project root; logs, sessions, and MCP config live in `.biofoundry/`.

## Git commit messages

Conventional Commits format:

```
<type>(<scope>): <subject>
```

Allowed types:
`feat`, `fix`, `test`, `refactor`, `chore`, `style`, `docs`, `perf`, `build`, `ci`, `revert`.

## Versioning

The project follows a **minor-bump-only** versioning scheme (`MAJOR.MINOR.PATCH`):

- **Patch** version is always `0`. Never bump it.
- **Minor** version is bumped for any change: new features, improvements, bug fixes, etc.
- **Major** version is only changed by explicit manual decision; it stays unchanged during
  normal development.

Examples: `0.68.0` → `0.69.0` → `0.70.0`; never `0.68.1`.

This rule applies to all packages in the repo (root, `packages/*`, `sdks/*`) as well as release
and skill workflows.

## Release workflow

1. Ensure `main` is up to date (pull latest).
2. Create a release branch, e.g. `bump-0.68` or `bump-biofoundry-os-0.5.3`.
3. Update `CHANGELOG.md`: rename `[Unreleased]` to `[0.68] - YYYY-MM-DD`.
4. Update `pyproject.toml` version.
5. Run `uv sync` to align `uv.lock`.
6. Commit the branch and open a PR.
7. Merge the PR, then switch back to `main` and pull latest.
8. Tag and push:
   - `git tag 0.68` or `git tag biofoundry-os-0.5.3`
   - `git push --tags`
9. GitHub Actions handles the release after tags are pushed.
