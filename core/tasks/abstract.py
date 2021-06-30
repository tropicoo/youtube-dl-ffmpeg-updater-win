import abc
import asyncio
import logging
import os
import re
from argparse import Namespace
from typing import Optional

from core.clients.abstract import AbstractApiClient
from core.clients.codexffmpeg import CodexFFAPIClient
from core.constants import CMD_FFMPEG_VERSION, FFMPEG_NUM_REGEX, RequiredFfbinaries
from core.utils import get_stdout


class AbstractUpdaterTask(abc.ABC):

    def __init__(self, api_client: AbstractApiClient, settings: Namespace):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)
        self._api = api_client
        self._settings = settings

    async def run(self) -> None:
        try:
            await self._update()
        finally:
            await self._cleanup()

    async def _cleanup(self) -> None:
        await self._api.close_session()

    @abc.abstractmethod
    async def _update(self) -> None:
        pass


class AbstractFFmpegUpdaterTask(AbstractUpdaterTask, abc.ABC):

    type: str = None
    _api: CodexFFAPIClient

    @abc.abstractmethod
    async def _perform_update(self) -> None:
        pass

    async def _update(self) -> None:
        """Update FFmpeg build."""
        self._log.info('Updating FFmpeg binaries from %s', self.type)
        if await self._needs_update():
            await self._perform_update()
        else:
            self._log.info('FFmpeg binaries are up-to-date, nothing to update')

    async def _needs_update(self) -> bool:
        """Check if ffbinaries need to be updated."""
        if self._settings.force or not self._all_ffbinaries_exist():
            return True

        latest_version, local_version = await asyncio.gather(self._api.get_latest_version(),
                                                             self._get_local_version())
        self._log.debug('Local FFmpeg version "%s", latest version "%s"', local_version, latest_version)
        if latest_version != local_version:
            self._log.info('Local FFmpeg build version %s needs update to %s',
                           local_version, latest_version)
            return True
        return False

    def _all_ffbinaries_exist(self) -> bool:
        """Check whether all FFmpeg binaries exist on disk."""
        files = os.listdir(self._settings.destination)
        return len(set(files) & RequiredFfbinaries.choices()) == len(RequiredFfbinaries)

    async def _get_local_version(self) -> Optional[str]:
        """Get local FFmpeg build numerical build version."""
        ffmpeg_ver = None
        bin_path = os.path.join(self._settings.destination, RequiredFfbinaries.FFMPEG.value)
        cmd = CMD_FFMPEG_VERSION.format(bin_path=bin_path)
        try:
            ffmpeg_ver = await get_stdout(cmd, self._log)
            ffmpeg_ver = ffmpeg_ver.splitlines()[0]
            ffmpeg_ver = re.search(FFMPEG_NUM_REGEX, ffmpeg_ver).group()
        except FileNotFoundError:
            self._log.warning('Local FFmpeg build not found, will proceed with download')
        except OSError as err:
            self._log.warning('Error getting local FFmpeg build version: %s', err)
        return ffmpeg_ver
