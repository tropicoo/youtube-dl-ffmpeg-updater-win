import asyncio
import logging
from pathlib import Path

import typer

from app.banner import BANNER
from app.constants import DEF_EXTRACT_PATH
from app.enums import (
    CodexSourceType,
    FFSourceType,
    LogLevel,
    UpdaterComponentType,
    WinPlatformType,
)
from app.log import init_logging
from app.settings import Settings
from app.updater import Updater


def main(  # noqa: PLR0913
    component: UpdaterComponentType = typer.Option(
        # UpdaterComponentType.ALL,
        UpdaterComponentType.FFMPEG,
        '-c',
        '--component',
        # help=f'updater components to update, default {UpdaterComponentType.ALL}', # noqa: ERA001
        help=f'updater components to update; currently, only "{UpdaterComponentType.FFMPEG}" is supported',
    ),
    destination: Path = typer.Option(
        DEF_EXTRACT_PATH,
        '-d',
        '--destination',
        exists=True,
        dir_okay=True,
        help='ffmpeg destination directory path',
    ),
    platform: WinPlatformType = typer.Option(
        WinPlatformType.WIN64,
        '-p',
        '--platform',
        help='ffmpeg binaries os platform',
    ),
    force: bool = typer.Option(False, '-f', '--force', help='perform force update'),  # noqa: FBT003
    ffmpeg_source: FFSourceType = typer.Option(
        FFSourceType.CODEX,
        '-fsrc',
        '--ffmpeg-source',
        help=f'ffmpeg binaries source; currently, only "{FFSourceType.CODEX}" is supported',
    ),
    codex_source: CodexSourceType = typer.Option(
        CodexSourceType.GITHUB,
        '-csrc',
        '--codex--source',
        help='codex binaries download source',
    ),
    verbose: int = typer.Option(
        LogLevel.INFO,
        '-v',
        '--verbose',
        min=LogLevel.ERROR,
        max=LogLevel.DEBUG,
        help='log level 0-3',
    ),
) -> None:
    settings = Settings(
        component=component,
        destination=destination,
        platform=platform,
        force=force,
        ffmpeg_source=ffmpeg_source,
        codex_source=codex_source,
        verbose=LogLevel(verbose),
    )
    init_logging(log_level=settings.verbose)

    logger = logging.getLogger(__name__)
    logger.info('\n%s', BANNER)
    logger.info('Starting main app')
    try:
        updater = Updater(settings=settings)
        # Not using "asyncio.run(main())" due to bug https://github.com/aio-libs/aiohttp/issues/4324
        asyncio.get_event_loop().run_until_complete(updater.run())
    finally:
        logger.info('Exiting main app')
