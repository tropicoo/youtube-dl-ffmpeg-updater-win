import os

import aiofiles

from core.clients.ytdl import YouTubeDLAPIClient
from core.constants import CMD_YOUTUBE_DL_UPDATE, EXE_YTDL
from core.tasks.abstract import AbstractUpdaterTask
from core.utils import get_stdout


class YTDLUpdaterTask(AbstractUpdaterTask):
    _api: YouTubeDLAPIClient

    def __init__(self, settings):
        super().__init__(api_client=YouTubeDLAPIClient(), settings=settings)

    async def _update(self) -> None:
        """Update youtube-dl from web or by subprocess."""
        self._log.info('Updating %s', EXE_YTDL)
        if self._settings.force:
            await self._update_from_web()
            return

        try:
            await self._update_by_subprocess()
        except Exception:
            self._log.warning('Local %s build not found, downloading from web', EXE_YTDL)
            await self._update_from_web()

    async def _update_from_web(self) -> None:
        """Update (download) youtube-dl from the web."""
        dest_path = os.path.join(self._settings.destination, EXE_YTDL)
        async with aiofiles.open(dest_path, 'wb') as f_out:
            async for chunk in self._api.download_latest_version():
                await f_out.write(chunk)
        await self._print_version()

    async def _update_by_subprocess(self) -> None:
        """Update youtube-dl by subprocess call."""
        bin_path = os.path.join(self._settings.destination, EXE_YTDL)
        cmd = CMD_YOUTUBE_DL_UPDATE.format(bin_path=bin_path)
        stdout = await get_stdout(cmd, self._log, raise_on_stderr=True)
        self._log.info('Command stdout "%s"', stdout.strip())

    async def _print_version(self) -> None:
        cmd = os.path.join(self._settings.destination, EXE_YTDL + ' --version')
        version = await get_stdout(cmd, self._log)
        self._log.info('youtube-dl updated to version %s',  version.strip())
