from __future__ import annotations

from typing import Any

from pygments.token import (
    Comment,
    Generic,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
)
from pygments.token import (
    Literal as PygmentsLiteral,
)
from pygments.token import (
    Text as PygmentsText,
)
from pygments.token import (
    Token as PygmentsToken,
)
from rich.style import Style
from rich.syntax import ANSISyntaxTheme, Syntax, SyntaxTheme

BIOFOUNDRY_ANSI_THEME_NAME = "biofoundry-ansi"
BIOFOUNDRY_ANSI_THEME = ANSISyntaxTheme(
    {
        PygmentsToken: Style(color="default"),
        PygmentsText: Style(color="default"),
        Comment: Style(color="#6a8f95", italic=True),
        Keyword: Style(color="#c88cff", bold=True),
        Keyword.Constant: Style(color="#c88cff", bold=True),
        Keyword.Declaration: Style(color="#c88cff", bold=True),
        Keyword.Namespace: Style(color="#c88cff", bold=True),
        Keyword.Pseudo: Style(color="#57e3d0"),
        Keyword.Reserved: Style(color="#c88cff", bold=True),
        Keyword.Type: Style(color="#57e3d0", bold=True),
        Name: Style(color="#e8fff8"),
        Name.Attribute: Style(color="#a8f56d"),
        Name.Builtin: Style(color="#a8f56d"),
        Name.Builtin.Pseudo: Style(color="#57e3d0"),
        Name.Builtin.Type: Style(color="#a8f56d", bold=True),
        Name.Class: Style(color="bright_white", bold=True),
        Name.Constant: Style(color="#ff8db6"),
        Name.Decorator: Style(color="#c88cff"),
        Name.Entity: Style(color="#57e3d0"),
        Name.Exception: Style(color="indian_red1", bold=True),
        Name.Function: Style(color="#57e3d0"),
        Name.Label: Style(color="#a8f56d"),
        Name.Namespace: Style(color="#a8f56d"),
        Name.Other: Style(color="#e8fff8"),
        Name.Property: Style(color="#a8f56d"),
        Name.Tag: Style(color="#ff8db6"),
        Name.Variable: Style(color="#e8fff8"),
        PygmentsLiteral: Style(color="#ff8db6"),
        PygmentsLiteral.Date: Style(color="#57e3d0"),
        String: Style(color="#7ce7ff"),
        String.Doc: Style(color="#7ce7ff", italic=True),
        String.Interpol: Style(color="#7ce7ff"),
        String.Affix: Style(color="#7ce7ff"),
        Number: Style(color="#a8f56d"),
        Operator: Style(color="default"),
        Punctuation: Style(color="default"),
        Generic.Deleted: Style(color="red3"),
        Generic.Emph: Style(italic=True),
        Generic.Error: Style(color="red3", bold=True),
        Generic.Heading: Style(color="#57e3d0", bold=True),
        Generic.Inserted: Style(color="#a8f56d"),
        Generic.Output: Style(color="#6a8f95"),
        Generic.Prompt: Style(color="#c88cff"),
        Generic.Strong: Style(bold=True),
        Generic.Subheading: Style(color="#a8f56d"),
        Generic.Traceback: Style(color="red3", bold=True),
    }
)


def resolve_code_theme(theme: str | SyntaxTheme) -> str | SyntaxTheme:
    if isinstance(theme, str) and theme.lower() == BIOFOUNDRY_ANSI_THEME_NAME:
        return BIOFOUNDRY_ANSI_THEME
    return theme


class BiofoundrySyntax(Syntax):
    def __init__(self, code: str, lexer: str, **kwargs: Any) -> None:
        if "theme" not in kwargs or kwargs["theme"] is None:
            kwargs["theme"] = BIOFOUNDRY_ANSI_THEME
        super().__init__(code, lexer, **kwargs)


if __name__ == "__main__":
    from rich.console import Console
    from rich.text import Text

    console = Console()

    examples = [
        ("diff", "diff", "@@ -1,2 +1,2 @@\n-line one\n+line uno\n"),
        (
            "python",
            "python",
            'def greet(name: str) -> str:\n    return f"Hi, {name}!"\n',
        ),
        ("bash", "bash", "set -euo pipefail\nprintf '%s\\n' \"hello\"\n"),
    ]

    for idx, (title, lexer, code) in enumerate(examples):
        if idx:
            console.print()
        console.print(Text(f"[{title}]", style="bold"))
        console.print(BiofoundrySyntax(code, lexer))
