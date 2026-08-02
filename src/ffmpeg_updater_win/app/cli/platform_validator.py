import platform

import typer

from ffmpeg_updater_win.app.constants import APP_NAME, WINDOWS_PLATFORM
from ffmpeg_updater_win.app.enums import ExitCodeType
from ffmpeg_updater_win.app.utils import print_bold_green, print_red
from ffmpeg_updater_win.app.version import __version__


def abort_on_non_windows() -> None:
    system = platform.system()
    if system != WINDOWS_PLATFORM:
        print_bold_green(f'{APP_NAME} {__version__}')
        print_red(f'Unsupported operating system: {system}')
        raise typer.Exit(code=ExitCodeType.EXIT_ERROR)
