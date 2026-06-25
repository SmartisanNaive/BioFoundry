# Changelog

All notable changes to written project materials (documentation, READMEs, user-facing docs) are tracked in this file.

## 2026-06-25

### Changed

- Rewrote `README.md` as the default Chinese version.
- Added `README.en.md` as the English translation.
- Simplified `README_zh.md` to a redirect pointing to `README.md` and `README.en.md`.
- Updated project READMEs to reflect the current feature set: Sanger sequencing analysis, unified `synpan` module (merged from `xingpan`), built-in MCP services, bundled Biofoundry skills, and multi-mode CLI usage.

## 2026-06-25

### Changed

- Merged `xingpan` module into `synpan`.
- Unified CLI command: `biofoundry synpan-mcp` now exposes both CIAI device-driver tools and third-party craft-platform tools.
- Replaced `--no-xingpan-mcp` with `--no-synpan-mcp`.
- Added `SYNPAN_PLATFORM_*` environment variables with legacy `XINGPAN_*` fallbacks.
- Merged `docs/xingpan-mcp.md` into `docs/synpan-mcp.md`.
- Combined `tests/test_xingpan_mcp.py` and `tests/test_synpan_mcp.py` into `tests/test_synpan_mcp.py`.

### Added

- Sanger sequencing analysis tool (`biofoundry_cli.tools.sanger.SangerAlign`).
- SynPan/CIAI device driver MCP adapter (`biofoundry_cli.synpan`).
- Bundled `sanger-sequencing-analysis` skill under `Knowledge/biofoundry-skills/skills/`.
