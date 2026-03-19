from __future__ import annotations

from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_submodules


def _collect_project_knowledge_files() -> list[tuple[str, str]]:
    """Collect root-level Knowledge files into the packaged biofoundry_cli/knowledge tree."""
    repo_root = Path(__file__).resolve().parents[3]
    knowledge_root = repo_root / "Knowledge"
    if not knowledge_root.is_dir():
        return []

    excluded_parts = {".venv", "__pycache__"}
    datas: list[tuple[str, str]] = []
    for file_path in knowledge_root.rglob("*"):
        if not file_path.is_file() or excluded_parts.intersection(file_path.parts):
            continue
        relative_parent = file_path.relative_to(knowledge_root).parent
        dest = Path("biofoundry_cli") / "knowledge" / relative_parent
        datas.append((str(file_path), str(dest)))
    return datas


hiddenimports = collect_submodules("biofoundry_cli.tools") + ["setproctitle"]
datas = (
    collect_data_files(
        "biofoundry_cli",
        includes=[
            "agents/**/*.yaml",
            "agents/**/*.md",
            "deps/bin/**",
            "prompts/**/*.md",
            "skills/**",
            "tools/**/*.md",
            "web/static/**",
            "vis/static/**",
            "CHANGELOG.md",
        ],
        excludes=[
            "tools/*.md",
        ],
    )
    + _collect_project_knowledge_files()
    + collect_data_files(
        "dateparser",
        includes=["**/*.pkl"],
    )
    + collect_data_files(
        "fastmcp",
        includes=["../fastmcp-*.dist-info/*"],
    )
)
