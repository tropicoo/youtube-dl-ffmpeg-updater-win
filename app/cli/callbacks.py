import typer
from rich import print as rich_print

from app.constants import APP_NAME
from app.version import __version__


def version_callback(value: bool) -> None:
    if value:
        rich_print(f'[green]{APP_NAME} CLI version:[/green] {__version__}')
        raise typer.Exit
