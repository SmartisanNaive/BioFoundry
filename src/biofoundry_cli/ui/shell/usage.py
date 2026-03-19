from __future__ import annotations

from biofoundry_cli.ui.shell.console import console
from biofoundry_cli.ui.shell.slash import registry


@registry.command(aliases=["/status"])
async def usage(app, args: str):
    """Display API usage and quota information"""
    del app, args
    console.print("[yellow]Usage reporting is not available in this fork.[/yellow]")
