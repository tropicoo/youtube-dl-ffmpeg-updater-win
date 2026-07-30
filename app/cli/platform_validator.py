import platform

import typer

from app.constants import APP_NAME, WINDOWS_PLATFORM
from app.enums import ExitCodeType
from app.utils import print_bold_green, print_red
from app.version import __version__


def abort_on_non_windows() -> None:
    system = platform.system()
    if system != WINDOWS_PLATFORM:
        print_bold_green(f'{APP_NAME} {__version__}')
        print_red(f'Unsupported operating system: {system}')
        raise typer.Exit(code=ExitCodeType.EXIT_ERROR)
