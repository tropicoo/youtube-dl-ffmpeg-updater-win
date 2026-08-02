import platform

import typer
from rich import print as rich_print
from rich.panel import Panel

from ffmpeg_updater_win.app.constants import APP_NAME, WINDOWS_PLATFORM
from ffmpeg_updater_win.app.enums import ExitCodeType
from ffmpeg_updater_win.app.version import __version__


def abort_on_non_windows() -> None:
    system = platform.system()
    if system != WINDOWS_PLATFORM:
        rich_print(
            Panel(
                f'[red]Unsupported system: {system}',
                title=f'{APP_NAME} {__version__}',
                border_style='red',
            )
        )
        raise typer.Exit(code=ExitCodeType.EXIT_ERROR)
