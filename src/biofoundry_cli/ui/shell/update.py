from __future__ import annotations

from enum import Enum, auto

from biofoundry_cli.share import get_share_dir
from biofoundry_cli.ui.shell.console import console
from biofoundry_cli.utils.logging import logger

UPGRADE_COMMAND = "manual installation required"
LATEST_VERSION_FILE = get_share_dir() / "latest_version.txt"


class UpdateResult(Enum):
    UPDATE_AVAILABLE = auto()
    UPDATED = auto()
    UP_TO_DATE = auto()
    FAILED = auto()
    UNSUPPORTED = auto()


def semver_tuple(version: str) -> tuple[int, int, int]:
    parts = version.strip().removeprefix("v").split(".")
    normalized = (parts + ["0", "0", "0"])[:3]
    try:
        return tuple(int(part) for part in normalized)  # type: ignore[return-value]
    except ValueError:
        return (0, 0, 0)


async def do_update(*, print: bool = True, check_only: bool = False) -> UpdateResult:
    del check_only
    logger.info("Auto-update is disabled in this fork.")
    if print:
        console.print("[yellow]Auto-update is disabled in this fork.[/yellow]")
    return UpdateResult.UNSUPPORTED
