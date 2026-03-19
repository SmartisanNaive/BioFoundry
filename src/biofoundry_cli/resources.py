from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path


def get_package_root_dir() -> Path:
    """Return the installed package root directory."""
    return Path(__file__).resolve().parent


def get_repo_root_candidate() -> Path:
    """Return the source-tree repository root when running from a checkout."""
    return get_package_root_dir().parent.parent


def _existing_unique_paths(paths: Iterable[Path]) -> tuple[Path, ...]:
    seen: set[str] = set()
    resolved_paths: list[Path] = []
    for path in paths:
        resolved = path.expanduser().resolve(strict=False)
        key = str(resolved)
        if key in seen or not resolved.exists():
            continue
        seen.add(key)
        resolved_paths.append(resolved)
    return tuple(resolved_paths)


def get_builtin_skills_dir_candidates() -> tuple[Path, ...]:
    """Return bundled skill directory candidates that do not depend on the current cwd."""
    repo_root = get_repo_root_candidate()
    return _existing_unique_paths(
        (
            get_package_root_dir() / "skills",
            get_package_root_dir() / "knowledge" / "biofoundry-skills",
            get_package_root_dir() / "knowledge" / "biofoundry-skills" / "skills",
            repo_root / "Knowledge" / "biofoundry-skills",
            repo_root / "Knowledge" / "biofoundry-skills" / "skills",
        )
    )


def get_builtin_knowledge_dir_candidates() -> tuple[Path, ...]:
    """Return bundled knowledge directory candidates that do not depend on the current cwd."""
    repo_root = get_repo_root_candidate()
    return _existing_unique_paths(
        (
            get_package_root_dir() / "knowledge",
            repo_root / "Knowledge",
        )
    )


def format_builtin_knowledge_index() -> str:
    """Build a compact index of bundled knowledge resources for the system prompt."""
    knowledge_roots = get_builtin_knowledge_dir_candidates()
    if not knowledge_roots:
        return "No bundled knowledge base found."

    lines: list[str] = []
    for root in knowledge_roots:
        lines.append(f"- Root: {root}")

        paper_dir = root / "Paper"
        if paper_dir.is_dir():
            paper_files = sorted(paper_dir.glob("*.md"))
            lines.append(f"  - Paper library: {paper_dir}")
            lines.append(f"  - Paper count: {len(paper_files)}")
            for paper in paper_files[:20]:
                lines.append(f"    - {paper.name}")
            if len(paper_files) > 20:
                lines.append(f"    - ... and {len(paper_files) - 20} more")

        skills_dir = root / "biofoundry-skills"
        if skills_dir.is_dir():
            lines.append(f"  - Biofoundry knowledge skills: {skills_dir}")

    return "\n".join(lines)
