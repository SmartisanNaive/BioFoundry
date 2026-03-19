from __future__ import annotations


class BiofoundryCLIException(Exception):
    """Base exception class for Biofoundry_CLI."""

    pass


class ConfigError(BiofoundryCLIException, ValueError):
    """Configuration error."""

    pass


class AgentSpecError(BiofoundryCLIException, ValueError):
    """Agent specification error."""

    pass


class InvalidToolError(BiofoundryCLIException, ValueError):
    """Invalid tool error."""

    pass


class SystemPromptTemplateError(BiofoundryCLIException, ValueError):
    """System prompt template error."""

    pass


class MCPConfigError(BiofoundryCLIException, ValueError):
    """MCP config error."""

    pass


class MCPRuntimeError(BiofoundryCLIException, RuntimeError):
    """MCP runtime error."""

    pass
