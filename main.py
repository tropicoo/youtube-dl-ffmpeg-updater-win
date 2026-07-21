import typer

from app.cli.main import run_cli


def main() -> None:
    typer.run(run_cli)


if __name__ == '__main__':
    main()
