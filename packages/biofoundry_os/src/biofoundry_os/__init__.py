from __future__ import annotations

import contextvars
from collections.abc import AsyncGenerator, AsyncIterator, Iterable, Mapping
from dataclasses import dataclass
from pathlib import PurePath
from typing import TYPE_CHECKING, Literal, Protocol, runtime_checkable

if TYPE_CHECKING:
    from asyncio import StreamReader, StreamWriter

    from asyncssh.stream import SSHReader, SSHWriter

    from biofoundry_os.path import FoundryPath

    def type_check(
        stream_reader: StreamReader,
        stream_writer: StreamWriter,
        ssh_reader: SSHReader[bytes],
        ssh_writer: SSHWriter[bytes],
    ):
        _reader: AsyncReadable = stream_reader
        _reader = ssh_reader
        _writer: AsyncWritable = stream_writer
        _writer = ssh_writer


type StrOrFoundryPath = str | FoundryPath


@runtime_checkable
class AsyncReadable(Protocol):
    """Protocol describing readable async byte streams."""

    def __aiter__(self) -> AsyncIterator[bytes]:
        """Yield chunks (typically lines) as they arrive."""
        ...

    def at_eof(self) -> bool:
        """Return True when the stream has reached EOF and buffer is empty."""
        ...

    def feed_data(self, data: bytes) -> None:
        """Inject data into the stream; mainly for testing or adapters."""
        ...

    def feed_eof(self) -> None:
        """Signal end-of-file to the stream."""
        ...

    async def read(self, n: int = -1) -> bytes:
        """Read up to n bytes; -1 reads until EOF."""
        ...

    async def readline(self) -> bytes:
        """Read a single line ending with newline or EOF."""
        ...

    async def readexactly(self, n: int) -> bytes:
        """Read exactly n bytes or raise IncompleteReadError."""
        ...

    async def readuntil(self, separator: bytes) -> bytes:
        """Read until separator is encountered, including the separator."""
        ...


@runtime_checkable
class AsyncWritable(Protocol):
    """Protocol describing writable async byte streams."""

    def can_write_eof(self) -> bool:
        """Return True if write_eof() is supported."""
        ...

    def close(self) -> None:
        """Schedule closing of the underlying transport."""
        ...

    async def drain(self) -> None:
        """Block until the internal write buffer is flushed."""
        ...

    def is_closing(self) -> bool:
        """Return True once the stream has been closed or is closing."""
        ...

    async def wait_closed(self) -> None:
        """Wait until the closing handshake completes."""
        ...

    def write(self, data: bytes) -> None:
        """Write raw bytes to the stream."""
        ...

    def writelines(self, data: Iterable[bytes], /) -> None:
        """Write an iterable of byte chunks to the stream."""
        ...

    def write_eof(self) -> None:
        """Send EOF to the underlying transport if supported."""
        ...


@runtime_checkable
class FoundryProcess(Protocol):
    """Process interface exposed by Foundry OS `exec` implementations."""

    stdin: AsyncWritable
    stdout: AsyncReadable
    stderr: AsyncReadable

    @property
    def pid(self) -> int:
        """Get the process ID."""
        ...

    @property
    def returncode(self) -> int | None:
        """Get the process return code, or None if it is still running."""
        ...

    async def wait(self) -> int:
        """Wait for the process to complete and return the exit code."""
        ...

    async def kill(self) -> None:
        """Kill the process."""
        ...


@runtime_checkable
class FoundryOS(Protocol):
    """Foundry OS interface."""

    name: str
    """The name of the Foundry OS implementation."""

    def pathclass(self) -> type[PurePath]:
        """Get the path class used under `FoundryPath`."""
        ...

    def normpath(self, path: StrOrFoundryPath) -> FoundryPath:
        """Normalize path, eliminating double slashes, etc."""
        ...

    def gethome(self) -> FoundryPath:
        """Get the home directory path."""
        ...

    def getcwd(self) -> FoundryPath:
        """Get the current working directory path."""
        ...

    async def chdir(self, path: StrOrFoundryPath) -> None:
        """Change the current working directory."""
        ...

    async def stat(self, path: StrOrFoundryPath, *, follow_symlinks: bool = True) -> StatResult:
        """Get the stat result for a path."""
        ...

    def iterdir(self, path: StrOrFoundryPath) -> AsyncGenerator[FoundryPath]:
        """Iterate over the entries in a directory."""
        ...

    def glob(
        self, path: StrOrFoundryPath, pattern: str, *, case_sensitive: bool = True
    ) -> AsyncGenerator[FoundryPath]:
        """Search for files/directories matching a pattern in the given path."""
        ...

    async def readbytes(self, path: StrOrFoundryPath, n: int | None = None) -> bytes:
        """Read the entire file contents as bytes, or the first n bytes if provided."""
        ...

    async def readtext(
        self,
        path: StrOrFoundryPath,
        *,
        encoding: str = "utf-8",
        errors: Literal["strict", "ignore", "replace"] = "strict",
    ) -> str:
        """Read the entire file contents as text."""
        ...

    def readlines(
        self,
        path: StrOrFoundryPath,
        *,
        encoding: str = "utf-8",
        errors: Literal["strict", "ignore", "replace"] = "strict",
    ) -> AsyncGenerator[str]:
        """Iterate over the lines of the file."""
        ...

    async def writebytes(self, path: StrOrFoundryPath, data: bytes) -> int:
        """Write bytes data to the file."""
        ...

    async def writetext(
        self,
        path: StrOrFoundryPath,
        data: str,
        *,
        mode: Literal["w", "a"] = "w",
        encoding: str = "utf-8",
        errors: Literal["strict", "ignore", "replace"] = "strict",
    ) -> int:
        """Write text data to the file, returning the number of characters written."""
        ...

    async def mkdir(
        self, path: StrOrFoundryPath, parents: bool = False, exist_ok: bool = False
    ) -> None:
        """Create a directory at the given path."""
        ...

    async def exec(self, *args: str, env: Mapping[str, str] | None = None) -> FoundryProcess:
        """
        Execute a command with arguments and return the running process.

        Args:
            *args: Command and its arguments.
            env: Environment variables for the subprocess. If None, inherits
                 from the parent process.
        """
        ...


@dataclass
class StatResult:
    """Foundry OS stat result data class."""

    st_mode: int
    st_ino: int
    st_dev: int
    st_nlink: int
    st_uid: int
    st_gid: int
    st_size: int
    st_atime: float
    st_mtime: float
    st_ctime: float


def get_current_foundry_os() -> FoundryOS:
    """Get the current Foundry OS instance."""
    from biofoundry_os._current import current_foundry_os

    return current_foundry_os.get()


def set_current_foundry_os(biofoundry_os: FoundryOS) -> contextvars.Token[FoundryOS]:
    """Set the current Foundry OS instance."""
    from biofoundry_os._current import current_foundry_os

    return current_foundry_os.set(biofoundry_os)


def reset_current_foundry_os(token: contextvars.Token[FoundryOS]) -> None:
    """Reset the current Foundry OS instance."""
    from biofoundry_os._current import current_foundry_os

    current_foundry_os.reset(token)


def pathclass() -> type[PurePath]:
    return get_current_foundry_os().pathclass()


def normpath(path: StrOrFoundryPath) -> FoundryPath:
    return get_current_foundry_os().normpath(path)


def gethome() -> FoundryPath:
    return get_current_foundry_os().gethome()


def getcwd() -> FoundryPath:
    return get_current_foundry_os().getcwd()


async def chdir(path: StrOrFoundryPath) -> None:
    await get_current_foundry_os().chdir(path)


async def stat(path: StrOrFoundryPath, *, follow_symlinks: bool = True) -> StatResult:
    return await get_current_foundry_os().stat(path, follow_symlinks=follow_symlinks)


def iterdir(path: StrOrFoundryPath) -> AsyncGenerator[FoundryPath]:
    return get_current_foundry_os().iterdir(path)


def glob(
    path: StrOrFoundryPath, pattern: str, *, case_sensitive: bool = True
) -> AsyncGenerator[FoundryPath]:
    return get_current_foundry_os().glob(path, pattern, case_sensitive=case_sensitive)


async def readbytes(path: StrOrFoundryPath, n: int | None = None) -> bytes:
    return await get_current_foundry_os().readbytes(path, n=n)


async def readtext(
    path: StrOrFoundryPath,
    *,
    encoding: str = "utf-8",
    errors: Literal["strict", "ignore", "replace"] = "strict",
) -> str:
    return await get_current_foundry_os().readtext(path, encoding=encoding, errors=errors)


def readlines(
    path: StrOrFoundryPath,
    *,
    encoding: str = "utf-8",
    errors: Literal["strict", "ignore", "replace"] = "strict",
) -> AsyncGenerator[str]:
    return get_current_foundry_os().readlines(path, encoding=encoding, errors=errors)


async def writebytes(path: StrOrFoundryPath, data: bytes) -> int:
    return await get_current_foundry_os().writebytes(path, data)


async def writetext(
    path: StrOrFoundryPath,
    data: str,
    *,
    mode: Literal["w", "a"] = "w",
    encoding: str = "utf-8",
    errors: Literal["strict", "ignore", "replace"] = "strict",
) -> int:
    return await get_current_foundry_os().writetext(
        path, data, mode=mode, encoding=encoding, errors=errors
    )


async def mkdir(path: StrOrFoundryPath, parents: bool = False, exist_ok: bool = False) -> None:
    return await get_current_foundry_os().mkdir(path, parents=parents, exist_ok=exist_ok)


async def exec(*args: str, env: Mapping[str, str] | None = None) -> FoundryProcess:
    return await get_current_foundry_os().exec(*args, env=env)
