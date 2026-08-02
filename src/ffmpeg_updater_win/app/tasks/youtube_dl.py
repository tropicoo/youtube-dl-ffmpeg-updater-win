from abc import ABC, abstractmethod
from typing import ClassVar

import aiofiles
from loguru import logger

from ffmpeg_updater_win.app.clients.ytdl import YTDLApiClient
from ffmpeg_updater_win.app.constants import (
    CMD_FFMPEG_VERSION_ARG,
    CMD_YOUTUBE_DL_UPDATE,
    EXE_YTDL,
)
from ffmpeg_updater_win.app.exceptions import CommandError
from ffmpeg_updater_win.app.models.config import UpdaterConfig
from ffmpeg_updater_win.app.tasks.abstract import BaseUpdaterTask
from ffmpeg_updater_win.app.utils import get_stdout


class BaseYTDLUpdater(ABC):
    NAME: ClassVar[str | None] = None

    def __init__(self, settings: UpdaterConfig) -> None:
        self._log = logger
        self._log.debug('Initializing "{}"', self.__class__.__name__)
        self._settings = settings

    async def _print_version(self) -> None:
        bin_path = (self._settings.destination / EXE_YTDL).as_posix()
        version = await get_stdout(
            cmd=(bin_path, CMD_FFMPEG_VERSION_ARG), log=self._log
        )
        self._log.info('youtube-dl updated to version {}', version.strip())

    async def update(self) -> None:
        self._log.info('Updating by {}', self.NAME)
        await self._update()

    @abstractmethod
    async def _update(self) -> None:
        pass


class YTDLWebUpdater(BaseYTDLUpdater):
    NAME: ClassVar[str] = 'youtube-dl web updater'

    def __init__(self, settings: UpdaterConfig, api_client: YTDLApiClient) -> None:
        super().__init__(settings=settings)
        self._api_client = api_client

    async def _update(self) -> None:
        """Update (download) youtube-dl from the web."""
        dest_path = self._settings.destination / EXE_YTDL
        async with aiofiles.open(dest_path, 'wb') as f_out:
            async for chunk in self._api_client.download_latest_version():
                await f_out.write(chunk)
        await self._print_version()


class YTDLSubprocessUpdater(BaseYTDLUpdater):
    NAME: ClassVar[str] = 'youtube-dl subprocess updater'

    async def _update(self) -> None:
        """Update youtube-dl by subprocess call."""
        bin_path = self._settings.destination / EXE_YTDL
        cmd = CMD_YOUTUBE_DL_UPDATE.format(bin_path=bin_path)
        stdout = await get_stdout((cmd,), self._log, raise_on_stderr=True)
        self._log.info('Command stdout "{}"', stdout.strip())


class YTDLUpdaterTask(BaseUpdaterTask[YTDLApiClient]):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._web_updater = YTDLWebUpdater(self._settings, self._api_client)
        self._subprocess_updater = YTDLSubprocessUpdater(self._settings)

    async def _update(self) -> None:
        """Update youtube-dl from web or by subprocess."""
        self._log.info('Updating {}', EXE_YTDL)
        if self._settings.force:
            await self._web_updater.update()
            return

        try:
            await self._subprocess_updater.update()
        except CommandError:
            self._log.warning(
                'Local {} build not found, downloading from web', EXE_YTDL
            )
            await self._web_updater.update()
