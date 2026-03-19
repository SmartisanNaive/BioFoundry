from __future__ import annotations

from typer.testing import CliRunner

from biofoundry_cli.cli import cli
from biofoundry_cli.constant import NAME
from biofoundry_cli.share import get_project_root, get_share_dir


def test_version_uses_biofoundry_brand() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])

    assert result.exit_code == 0
    assert "biofoundry, version" in result.stdout


def test_constant_name_is_rebranded() -> None:
    assert NAME == "Biofoundry_CLI"


def test_share_dir_uses_biofoundry_env_var(monkeypatch, tmp_path) -> None:
    override = tmp_path / "share"
    monkeypatch.setenv("BIOFOUNDRY_SHARE_DIR", str(override))

    path = get_share_dir()

    assert path == override
    assert path.exists()


def test_share_dir_defaults_to_project_root(monkeypatch, tmp_path) -> None:
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'demo'\n", encoding="utf-8")
    monkeypatch.delenv("BIOFOUNDRY_SHARE_DIR", raising=False)
    monkeypatch.chdir(tmp_path)

    assert get_project_root() == tmp_path
    assert get_share_dir() == tmp_path / ".biofoundry"
