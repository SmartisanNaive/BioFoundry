# Changelog

## Unreleased

## 0.7.0 (2026-02-06)

- Add `env` parameter to `exec()` method for passing environment variables to subprocesses

## 0.6.0 (2026-01-09)

- Add optional `n` parameter to `readbytes` to read only the first n bytes

## 0.5.4 (2026-01-06)

- Relax `aiofiles` dependency version to `>=24.0,<26.0`

## 0.5.3 (2025-12-29)

- Add `host` property to `SSHFoundryOS`

## 0.5.2 (2025-12-17)

- Fix `SSHFoundryOS.Process.wait` to not drain stdout/stderr buffers
- Return 1 as return code if `SSHFoundryOS.Process.wait` does not get a return code

## 0.5.1 (2025-12-15)

- Fix unhandled exception thrown by `SSHFoundryOS.stat` when the file does not exist
- Fix `SSHFoundryOS.exec` without CWD
- Fix `SSHFoundryOS.iterdir` to return `FoundryPath`

## 0.5.0 (2025-12-12)

- Move `FoundryProcess` to `FoundryOS.Process`
- Add `AsyncReadable` and `AsyncWritable` protocols
- Add `SSHFoundryOS` implementation
- Lower the required Python version to 3.12

## 0.4.0 (2025-12-06)

- Add `FoundryOS.exec` method for executing commands
- Add `StepResult` as the return type for `FoundryOS.stat`

## 0.3.0 (2025-12-03)

- Change `iterdir`, `glob` and `read_lines` to sync function returning `AsyncIterator`

## 0.2.0 (2025-12-01)

- Initial release with `FoundryOS` protocol, `LocalFoundryOS` implementation, and `FoundryPath` for convenient file operations
