import logging
from abc import ABC, abstractmethod

import aiofiles

from app.clients.ytdl import YTDLApiClient
from app.constants import CMD_FFMPEG_VERSION_ARG, CMD_YOUTUBE_DL_UPDATE, EXE_YTDL
from app.exceptions import CommandError
from app.settings import Settings
from app.tasks.abstract import AbstractUpdaterTask
from app.utils import get_stdout


class AbstractYTDLUpdater(ABC):
    NAME: str | None = None

    def __init__(self, settings: Settings) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing "%s"', self.__class__.__name__)
        self._settings = settings

    async def _print_version(self) -> None:
        bin_path = (self._settings.destination / EXE_YTDL).as_posix()
        version = await get_stdout(
            cmd=(bin_path, CMD_FFMPEG_VERSION_ARG), log=self._log
        )
        self._log.info('youtube-dl updated to version %s', version.strip())

    async def update(self) -> None:
        self._log.info('Updating by %s', self.NAME)
        await self._update()

    @abstractmethod
    async def _update(self) -> None:
        pass


class YTDLWebUpdater(AbstractYTDLUpdater):
    NAME: str = 'youtube-dl web updater'

    def __init__(self, settings: Settings, api_client: YTDLApiClient) -> None:
        super().__init__(settings=settings)
        self._api_client = api_client

    async def _update(self) -> None:
        """Update (download) youtube-dl from the web."""
        dest_path = self._settings.destination / EXE_YTDL
        async with aiofiles.open(dest_path, 'wb') as f_out:
            async for chunk in self._api_client.download_latest_version():
                await f_out.write(chunk)
        await self._print_version()


class YTDLSubprocessUpdater(AbstractYTDLUpdater):
    NAME: str = 'youtube-dl subprocess updater'

    async def _update(self) -> None:
        """Update youtube-dl by subprocess call."""
        bin_path = self._settings.destination / EXE_YTDL
        cmd = CMD_YOUTUBE_DL_UPDATE.format(bin_path=bin_path)
        stdout = await get_stdout((cmd,), self._log, raise_on_stderr=True)
        self._log.info('Command stdout "%s"', stdout.strip())


class YTDLUpdaterTask(AbstractUpdaterTask):
    _api_client: YTDLApiClient

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._web_updater = YTDLWebUpdater(self._settings, self._api_client)
        self._subprocess_updater = YTDLSubprocessUpdater(self._settings)

    async def _update(self) -> None:
        """Update youtube-dl from web or by subprocess."""
        self._log.info('Updating %s', EXE_YTDL)
        if self._settings.force:
            await self._web_updater.update()
            return

        try:
            await self._subprocess_updater.update()
        except CommandError:
            self._log.warning(
                'Local %s build not found, downloading from web', EXE_YTDL
            )
            await self._web_updater.update()
