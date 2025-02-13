import asyncio
import logging
from pathlib import Path

import typer

from core.constants import DEF_EXTRACT_PATH
from core.enums import (
    CodexSourceType,
    FFSourceType,
    LogLevel,
    UpdaterComponentType,
    WinPlatformType,
)
from core.log import init_logging
from core.settings import Settings
from core.updater import Updater


def main(
    component: UpdaterComponentType = typer.Option(
        UpdaterComponentType.ALL,
        '-c',
        '--component',
        help=f'updater components to update, default {UpdaterComponentType.ALL}',
    ),
    destination: Path = typer.Option(
        DEF_EXTRACT_PATH,
        '-d',
        '--destination',
        exists=True,
        dir_okay=True,
        help='youtube-dl directory path',
    ),
    platform: WinPlatformType = typer.Option(
        WinPlatformType.WIN64,
        '-p',
        '--platform',
        help='ffmpeg binaries os platform',
    ),
    force: bool = typer.Option(False, '-f', '--force', help='perform force update'),
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
        LogLevel.INFO.value,
        '-v',
        '--verbose',
        min=LogLevel.ERROR.value,
        max=LogLevel.DEBUG.value,
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
    logger.info('Starting main app')
    try:
        updater = Updater(settings=settings)
        # Not using "asyncio.run(main())" due to bug https://github.com/aio-libs/aiohttp/issues/4324
        asyncio.get_event_loop().run_until_complete(updater.run())
    finally:
        logger.info('Exiting main app')
