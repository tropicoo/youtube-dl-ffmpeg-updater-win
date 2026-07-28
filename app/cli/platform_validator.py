import platform

import typer

from app.constants import EXIT_ERROR, WINDOWS_PLATFORM
from app.utils import print_bold_red


def abort_on_non_windows() -> None:
    system = platform.system()
    if system != WINDOWS_PLATFORM:
        print_bold_red(f'Unsupported operating system: {system}')
        raise typer.Exit(code=EXIT_ERROR)
