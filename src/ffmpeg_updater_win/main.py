import typer

from ffmpeg_updater_win.app.cli.main import run_cli


def main() -> None:
    typer.run(run_cli)
