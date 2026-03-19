from __future__ import annotations

from rich.console import Console
from rich.theme import Theme

NEUTRAL_MARKDOWN_THEME = Theme(
    {
        "markdown.paragraph": "#e8fff8",
        "markdown.block_quote": "grey62 italic",
        "markdown.hr": "#31545a",
        "markdown.item": "#e8fff8",
        "markdown.item.bullet": "#57e3d0",
        "markdown.item.number": "#57e3d0",
        "markdown.link": "underline #57e3d0",
        "markdown.link_url": "underline #c88cff",
        "markdown.h1": "bold #57e3d0",
        "markdown.h1.border": "#57e3d0",
        "markdown.h2": "bold #c88cff",
        "markdown.h3": "bold #a8f56d",
        "markdown.h4": "bold #d8fff4",
        "markdown.h5": "bold grey78",
        "markdown.h6": "grey62 italic",
        "markdown.em": "none",
        "markdown.strong": "none",
        "markdown.s": "none",
        "status.spinner": "#57e3d0",
    },
    inherit=True,
)

_NEUTRAL_MARKDOWN_THEME = NEUTRAL_MARKDOWN_THEME
console = Console(highlight=False, theme=NEUTRAL_MARKDOWN_THEME)
