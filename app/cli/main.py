import asyncio
import logging
from pathlib import Path
from typing import Annotated

import typer

from app.banner import BANNER
from app.cli.callbacks import version_callback
from app.cli.platform_validator import abort_on_non_windows
from app.constants import DEF_EXTRACT_PATH
from app.core.updater import Updater
from app.enums import (
    CodexSourceType,
    FFSourceType,
    LogLevelType,
    UpdaterComponentType,
    WinPlatformType,
)
from app.log import init_logging
from app.settings import Settings


def run_cli(  # noqa: PLR0913, PLR0917
    component: UpdaterComponentType = typer.Option(
        # UpdaterComponentType.ALL,
        UpdaterComponentType.FFMPEG,
        '-c',
        '--component',
        # help=f'updater components to update, default {UpdaterComponentType.ALL}', # noqa: ERA001
        help=f'Updater components to update; currently, only "{UpdaterComponentType.FFMPEG}" is supported',
    ),
    destination: Path = typer.Option(
        DEF_EXTRACT_PATH,
        '-d',
        '--destination',
        file_okay=False,
        dir_okay=True,
        help='Ffmpeg destination directory path',
    ),
    platform: WinPlatformType = typer.Option(
        WinPlatformType.WIN64,
        '-p',
        '--platform',
        help='Ffmpeg binaries os platform',
    ),
    force: bool = typer.Option(False, '-f', '--force', help='Perform force update'),  # noqa: FBT003
    ffmpeg_source: FFSourceType = typer.Option(
        FFSourceType.CODEX,
        '-fsrc',
        '--ffmpeg-source',
        help=f'Ffmpeg binaries source; currently, only "{FFSourceType.CODEX}" is supported',
    ),
    codex_source: CodexSourceType = typer.Option(
        CodexSourceType.GITHUB,
        '-csrc',
        '--codex--source',
        help='Codex binaries download source',
    ),
    verbose: LogLevelType = typer.Option(
        LogLevelType.INFO, '-v', '--verbose', help='Log level 0-3'
    ),
    version: Annotated[  # noqa: ARG001
        bool | None,
        typer.Option(
            '-V', '--version', callback=version_callback, help='Show app version'
        ),
    ] = None,
) -> None:
    abort_on_non_windows()
    settings = Settings(
        component=component,
        destination=destination,
        platform=platform,
        force=force,
        ffmpeg_source=ffmpeg_source,
        codex_source=codex_source,
        verbose=LogLevelType(verbose),
    )
    init_logging(log_level=settings.verbose)

    logger = logging.getLogger(__name__)
    logger.info('\n%s', BANNER)
    logger.info('Starting main app')
    try:
        asyncio.run(Updater(settings=settings).run())
    finally:
        logger.info('Exiting main app')
