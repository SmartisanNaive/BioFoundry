from __future__ import annotations

import json
from hashlib import md5
from pathlib import Path

from biofoundry_os import get_current_foundry_os
from biofoundry_os.local import local_foundry_os
from biofoundry_os.path import FoundryPath
from pydantic import BaseModel, ConfigDict, Field

from biofoundry_cli.share import get_share_dir
from biofoundry_cli.utils.io import atomic_json_write
from biofoundry_cli.utils.logging import logger


def get_metadata_file() -> Path:
    return get_share_dir() / "metadata.json"


class WorkDirMeta(BaseModel):
    """Metadata for a work directory."""

    path: str
    """The full path of the work directory."""

    foundry_os: str = local_foundry_os.name
    """The name of the Foundry OS where the work directory is located."""

    last_session_id: str | None = None
    """Last session ID of this work directory."""

    @property
    def sessions_dir(self) -> Path:
        """The directory to store sessions for this work directory."""
        path_md5 = md5(self.path.encode(encoding="utf-8")).hexdigest()
        dir_basename = (
            path_md5
            if self.foundry_os == local_foundry_os.name
            else f"{self.foundry_os}_{path_md5}"
        )
        session_dir = get_share_dir() / "sessions" / dir_basename
        session_dir.mkdir(parents=True, exist_ok=True)
        return session_dir


class Metadata(BaseModel):
    """Biofoundry_CLI metadata structure."""

    model_config = ConfigDict(extra="ignore")

    work_dirs: list[WorkDirMeta] = Field(default_factory=list[WorkDirMeta])
    """Work directory list."""

    def get_work_dir_meta(self, path: FoundryPath) -> WorkDirMeta | None:
        """Get the metadata for a work directory."""
        for wd in self.work_dirs:
            if wd.path == str(path) and wd.foundry_os == get_current_foundry_os().name:
                return wd
        return None

    def new_work_dir_meta(self, path: FoundryPath) -> WorkDirMeta:
        """Create a new work directory metadata."""
        wd_meta = WorkDirMeta(path=str(path), foundry_os=get_current_foundry_os().name)
        self.work_dirs.append(wd_meta)
        return wd_meta


def load_metadata() -> Metadata:
    metadata_file = get_metadata_file()
    logger.debug("Loading metadata from file: {file}", file=metadata_file)
    if not metadata_file.exists():
        logger.debug("No metadata file found, creating empty metadata")
        return Metadata()
    with open(metadata_file, encoding="utf-8") as f:
        data = json.load(f)
        return Metadata(**data)


def save_metadata(metadata: Metadata):
    metadata_file = get_metadata_file()
    logger.debug("Saving metadata to file: {file}", file=metadata_file)
    atomic_json_write(metadata.model_dump(), metadata_file)
