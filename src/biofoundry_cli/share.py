from __future__ import annotations

import os
from pathlib import Path

_PROJECT_ROOT_MARKERS = ("pyproject.toml", "AGENTS.md", "config.example.toml", ".git")


def get_project_root(start: Path | None = None) -> Path:
    """Detect the current project root from the working directory."""
    current = (start or Path.cwd()).expanduser().resolve()
    for candidate in (current, *current.parents):
        if any((candidate / marker).exists() for marker in _PROJECT_ROOT_MARKERS):
            return candidate
    return current


def get_share_dir() -> Path:
    """Get the project-local share directory path."""
    if share_dir := os.getenv("BIOFOUNDRY_SHARE_DIR"):
        share_dir = Path(share_dir)
    else:
        share_dir = get_project_root() / ".biofoundry"
    share_dir.mkdir(parents=True, exist_ok=True)
    return share_dir
