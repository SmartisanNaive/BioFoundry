from __future__ import annotations

import pytest
from typer.testing import CliRunner

from biofoundry_cli.cli import cli
from biofoundry_cli.config import ConfigError, get_default_config, load_config


def test_login_and_logout_commands_are_removed() -> None:
    runner = CliRunner()

    login_result = runner.invoke(cli, ["login"])
    logout_result = runner.invoke(cli, ["logout"])

    assert login_result.exit_code != 0
    assert "No such command" in (login_result.stdout + login_result.stderr)
    assert logout_result.exit_code != 0
    assert "No such command" in (logout_result.stdout + logout_result.stderr)


def test_help_does_not_advertise_login_commands() -> None:
    runner = CliRunner()

    result = runner.invoke(cli, ["--help"])

    assert result.exit_code == 0
    assert " login " not in result.stdout
    assert " logout " not in result.stdout


def test_default_config_uses_openai_providers() -> None:
    config = get_default_config()

    assert config.default_model == "openai-responses"
    assert config.providers["openai-responses"].type == "openai_responses"
    assert config.providers["openai-legacy"].type == "openai_legacy"
    assert config.models["openai-responses"].provider == "openai-responses"
    assert config.models["openai-legacy"].provider == "openai-legacy"


def test_load_config_requires_existing_file(tmp_path) -> None:
    missing = tmp_path / "missing.toml"

    with pytest.raises(ConfigError, match="Config file not found"):
        load_config(missing)


def test_load_config_rejects_empty_stub_file(tmp_path) -> None:
    stub = tmp_path / "config.toml"
    stub.write_text(
        """\
default_model = ""
default_thinking = false
default_yolo = false
default_editor = ""

[models]

[providers]
""",
        encoding="utf-8",
    )

    with pytest.raises(ConfigError, match="default_model must be set|At least one model"):
        load_config(stub)


def test_load_config_accepts_generic_service_names(tmp_path) -> None:
    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """\
default_model = "openai-responses"
default_thinking = false
default_yolo = false
default_editor = ""

[models.openai-responses]
provider = "openai-responses"
model = "gpt-5"
max_context_size = 100000

[providers.openai-responses]
type = "openai_responses"
base_url = "https://api.openai.com/v1"
api_key = ""

[services.search]
base_url = "https://example.com/search"
api_key = ""

[services.fetch]
base_url = "https://example.com/fetch"
api_key = ""
""",
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert config.services.search is not None
    assert config.services.fetch is not None
    assert config.services.search.base_url == "https://example.com/search"
    assert config.services.fetch.base_url == "https://example.com/fetch"


def test_load_config_rejects_removed_legacy_provider_type(tmp_path) -> None:
    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """\
default_model = "removed-legacy-provider"
default_thinking = false
default_yolo = false
default_editor = ""

[models.removed-legacy-provider]
provider = "removed-legacy-provider"
model = "removed-model"
max_context_size = 100000

[providers.removed-legacy-provider]
type = "removed_provider_type"
base_url = "https://example.com/v1"
api_key = ""
""",
        encoding="utf-8",
    )

    with pytest.raises(ConfigError, match="type"):
        load_config(config_file)
