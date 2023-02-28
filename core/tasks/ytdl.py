import abc
import logging
import os

import aiofiles
from core.clients.ytdl import YTDLApiClient
from core.constants import CMD_YOUTUBE_DL_UPDATE, EXE_YTDL
from core.exceptions import CommandError
from core.tasks.abstract import AbstractUpdaterTask
from core.utils import get_stdout


class AbstractYTDLUpdater(abc.ABC):
    name: str

    def __init__(self, settings) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)
        self._settings = settings

    async def _print_version(self) -> None:
        cmd = os.path.join(self._settings.destination, EXE_YTDL + ' --version')
        version = await get_stdout(cmd, self._log)
        self._log.info('youtube-dl updated to version %s', version.strip())

    async def update(self) -> None:
        self._log.info('Updating by %s', self.name)
        await self._update()

    @abc.abstractmethod
    async def _update(self) -> None:
        pass


class YTDLWebUpdater(AbstractYTDLUpdater):
    name = 'youtube-dl web updater'

    def __init__(self, settings, api_client) -> None:
        super().__init__(settings)
        self._api = api_client

    async def _update(self) -> None:
        """Update (download) youtube-dl from the web."""
        dest_path = os.path.join(self._settings.destination, EXE_YTDL)
        async with aiofiles.open(dest_path, 'wb') as f_out:
            async for chunk in self._api.download_latest_version():
                await f_out.write(chunk)
        await self._print_version()


class YTDLSubprocessUpdater(AbstractYTDLUpdater):
    name = 'youtube-dl subprocess updater'

    async def _update(self) -> None:
        """Update youtube-dl by subprocess call."""
        bin_path = os.path.join(self._settings.destination, EXE_YTDL)
        cmd = CMD_YOUTUBE_DL_UPDATE.format(bin_path=bin_path)
        stdout = await get_stdout(cmd, self._log, raise_on_stderr=True)
        self._log.info('Command stdout "%s"', stdout.strip())


class YTDLUpdaterTask(AbstractUpdaterTask):
    _api: YTDLApiClient
    _web_updater_cls = YTDLWebUpdater
    _subprocess_updater_cls = YTDLSubprocessUpdater

    def __init__(self, settings) -> None:
        super().__init__(api_client=YTDLApiClient(), settings=settings)
        self._web_updater = self._web_updater_cls(self._settings, self._api)
        self._subprocess_updater = self._subprocess_updater_cls(self._settings)

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
