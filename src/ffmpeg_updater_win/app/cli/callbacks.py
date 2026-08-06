import typer
from rich import print as rich_print

from ffmpeg_updater_win.app.constants import APP_NAME, APP_VERSION


def version_callback(value: bool) -> None:
    if value:
        rich_print(f'[green]{APP_NAME} CLI version:[/green] {APP_VERSION}')
        raise typer.Exit
