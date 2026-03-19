from __future__ import annotations

from collections.abc import AsyncGenerator
from pathlib import Path, PurePath
from stat import S_ISDIR, S_ISREG
from typing import Any, Literal

import biofoundry_os


class FoundryPath:
    """
    A path abstraction for Foundry OS filesystem.
    """

    def __init__(self, *args: str) -> None:
        self._path: PurePath = biofoundry_os.pathclass()(*args)

    @classmethod
    def unsafe_from_local_path(cls, path: Path) -> FoundryPath:
        """
        Create a `FoundryPath` from a local `Path`.
        Only use this if you are sure that `LocalFoundryOS` is being used.
        """
        return cls(str(path))

    def unsafe_to_local_path(self) -> Path:
        """
        Convert the `FoundryPath` to a local `Path`.
        Only use this if you are sure that `LocalFoundryOS` is being used.
        """
        return Path(str(self._path))

    def __lt__(self, other: FoundryPath) -> bool:
        return self._path.__lt__(other._path)

    def __le__(self, other: FoundryPath) -> bool:
        return self._path.__le__(other._path)

    def __gt__(self, other: FoundryPath) -> bool:
        return self._path.__gt__(other._path)

    def __ge__(self, other: FoundryPath) -> bool:
        return self._path.__ge__(other._path)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FoundryPath):
            return NotImplemented
        return self._path.__eq__(other._path)

    def __repr__(self) -> str:
        return f"FoundryPath({repr(str(self._path))})"

    def __str__(self) -> str:
        return str(self._path)

    @property
    def name(self) -> str:
        """Return the final component of the path."""
        return self._path.name

    @property
    def parent(self) -> FoundryPath:
        """Return the parent directory of the path."""
        return FoundryPath(str(self._path.parent))

    def is_absolute(self) -> bool:
        """Return True if the path is absolute."""
        return self._path.is_absolute()

    def joinpath(self, *other: str) -> FoundryPath:
        """Join this path with other path components."""
        return FoundryPath(str(self._path.joinpath(*other)))

    def __truediv__(self, other: str | FoundryPath) -> FoundryPath:
        """Join this path with another path using the `/` operator."""
        p = other._path if isinstance(other, FoundryPath) else other
        ret = FoundryPath()
        ret._path = self._path.__truediv__(p)
        return ret

    def canonical(self) -> FoundryPath:
        """
        Make the path absolute, resolving all `.` and `..` in the path.
        Unlike `pathlib.Path.resolve`, this method does not resolve symlinks.
        """
        abs_path = self if self.is_absolute() else biofoundry_os.getcwd().joinpath(str(self._path))
        # Normalize the path (handle . and ..) but preserve the format
        normalized = biofoundry_os.normpath(abs_path)
        # `normpath` might strip trailing slash, but we want to preserve it for directories
        # However, since we don't access the filesystem, we can't know if it's a directory
        # So we follow the pathlib behavior which doesn't preserve trailing slashes
        return normalized

    def relative_to(self, other: FoundryPath) -> FoundryPath:
        """Return the relative path from `other` to this path."""
        relative_path = self._path.relative_to(other._path)
        return FoundryPath(str(relative_path))

    @classmethod
    def home(cls) -> FoundryPath:
        """Return the home directory as a FoundryPath."""
        return biofoundry_os.gethome()

    @classmethod
    def cwd(cls) -> FoundryPath:
        """Return the current working directory as a FoundryPath."""
        return biofoundry_os.getcwd()

    def expanduser(self) -> FoundryPath:
        """Expand `~` to the backend home directory."""
        parts = self._path.parts
        if not parts or parts[0] != "~":
            return self

        home = FoundryPath.home()
        if len(parts) == 1:
            return home
        return home.joinpath(*parts[1:])

    async def stat(self, follow_symlinks: bool = True) -> biofoundry_os.StatResult:
        """Return an os.stat_result for the path."""
        return await biofoundry_os.stat(self, follow_symlinks=follow_symlinks)

    async def exists(self, *, follow_symlinks: bool = True) -> bool:
        """Return True if the path points to an existing filesystem entry."""
        try:
            await self.stat(follow_symlinks=follow_symlinks)
            return True
        except OSError:
            return False

    async def is_file(self, *, follow_symlinks: bool = True) -> bool:
        """Return True if the path points to a regular file."""
        try:
            st = await self.stat(follow_symlinks=follow_symlinks)
            return S_ISREG(st.st_mode)
        except OSError:
            return False

    async def is_dir(self, *, follow_symlinks: bool = True) -> bool:
        """Return True if the path points to a directory."""
        try:
            st = await self.stat(follow_symlinks=follow_symlinks)
            return S_ISDIR(st.st_mode)
        except OSError:
            return False

    def iterdir(self) -> AsyncGenerator[FoundryPath]:
        """Return the direct children of the directory."""
        return biofoundry_os.iterdir(self)

    def glob(self, pattern: str, *, case_sensitive: bool = True) -> AsyncGenerator[FoundryPath]:
        """Return all paths matching the pattern under this directory."""
        return biofoundry_os.glob(self, pattern, case_sensitive=case_sensitive)

    async def read_bytes(self, n: int | None = None) -> bytes:
        """Read the entire file contents as bytes, or the first n bytes if provided."""
        return await biofoundry_os.readbytes(self, n=n)

    async def read_text(
        self,
        *,
        encoding: str = "utf-8",
        errors: Literal["strict", "ignore", "replace"] = "strict",
    ) -> str:
        """Read the entire file contents as text."""
        return await biofoundry_os.readtext(self, encoding=encoding, errors=errors)

    def read_lines(
        self,
        *,
        encoding: str = "utf-8",
        errors: Literal["strict", "ignore", "replace"] = "strict",
    ) -> AsyncGenerator[str]:
        """Iterate over the lines of the file."""
        return biofoundry_os.readlines(self, encoding=encoding, errors=errors)

    async def write_bytes(self, data: bytes) -> int:
        """Write bytes data to the file."""
        return await biofoundry_os.writebytes(self, data)

    async def write_text(
        self,
        data: str,
        *,
        encoding: str = "utf-8",
        errors: Literal["strict", "ignore", "replace"] = "strict",
    ) -> int:
        """Write text data to the file, returning the number of characters written."""
        return await biofoundry_os.writetext(
            self,
            data,
            mode="w",
            encoding=encoding,
            errors=errors,
        )

    async def append_text(
        self,
        data: str,
        *,
        encoding: str = "utf-8",
        errors: Literal["strict", "ignore", "replace"] = "strict",
    ) -> int:
        """Append text data to the file, returning the number of characters written."""
        return await biofoundry_os.writetext(
            self,
            data,
            mode="a",
            encoding=encoding,
            errors=errors,
        )

    async def mkdir(self, parents: bool = False, exist_ok: bool = False) -> None:
        """Create a directory at this path."""
        return await biofoundry_os.mkdir(self, parents=parents, exist_ok=exist_ok)
