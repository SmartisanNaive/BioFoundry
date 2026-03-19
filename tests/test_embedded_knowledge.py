from __future__ import annotations

from pathlib import Path

import pytest
from biofoundry_os.path import FoundryPath

from biofoundry_cli.config import get_default_config
from biofoundry_cli.resources import (
    format_builtin_knowledge_index,
    get_builtin_knowledge_dir_candidates,
    get_builtin_skills_dir_candidates,
)
from biofoundry_cli.session import Session
from biofoundry_cli.skill import discover_skills_from_roots, resolve_skills_roots
from biofoundry_cli.soul.agent import Runtime


def test_builtin_resource_candidates_include_repo_knowledge() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    knowledge_root = repo_root / "Knowledge"

    assert knowledge_root in get_builtin_knowledge_dir_candidates()
    assert (knowledge_root / "biofoundry-skills") in get_builtin_skills_dir_candidates()


def test_builtin_knowledge_index_mentions_papers() -> None:
    knowledge_index = format_builtin_knowledge_index()

    assert "Paper library" in knowledge_index
    assert "Paper count" in knowledge_index
    assert "Knowledge" in knowledge_index


@pytest.mark.asyncio
async def test_discover_skills_from_embedded_roots(tmp_path: Path) -> None:
    work_dir = FoundryPath.unsafe_from_local_path(tmp_path)

    roots = await resolve_skills_roots(work_dir)
    skills = await discover_skills_from_roots(roots)
    skill_names = {skill.name for skill in skills}

    assert "sequence-space-parser" in skill_names
    assert "dna-assembly" in skill_names


@pytest.mark.asyncio
async def test_runtime_exposes_embedded_knowledge_dirs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    work_dir = tmp_path / "workspace"
    work_dir.mkdir()
    monkeypatch.setenv("BIOFOUNDRY_SHARE_DIR", str(tmp_path / "share"))

    session = await Session.create(FoundryPath.unsafe_from_local_path(work_dir))
    runtime = await Runtime.create(
        config=get_default_config(),
        llm=None,
        session=session,
        yolo=False,
    )

    additional_dirs = {Path(str(path)).resolve(strict=False) for path in runtime.additional_dirs}

    assert (Path(__file__).resolve().parent.parent / "Knowledge") in additional_dirs
    assert "Paper library" in runtime.builtin_args.BIOFOUNDRY_KNOWLEDGE
