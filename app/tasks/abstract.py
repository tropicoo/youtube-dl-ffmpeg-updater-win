import asyncio
import logging
import re
from abc import ABC, abstractmethod

from app.clients.abstract import AbstractApiClient
from app.clients.codexffmpeg import AbstractCodexFFAPIClient
from app.constants import CMD_FFMPEG_VERSION_ARG, FFMPEG_NUM_REGEX
from app.enums import FFSourceType, RequiredFfbinaryType
from app.settings import Settings
from app.utils import get_stdout


class AbstractUpdaterTask(ABC):
    def __init__(self, api_client: AbstractApiClient, settings: Settings) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing "%s"', self.__class__.__name__)
        self._api_client = api_client
        self._settings = settings

    async def run(self) -> None:
        try:
            await self._update()
        finally:
            await self._cleanup()

    async def _cleanup(self) -> None:
        await self._api_client.close_session()

    @abstractmethod
    async def _update(self) -> None:
        pass


class AbstractFFmpegUpdaterTask(AbstractUpdaterTask, ABC):
    TYPE: FFSourceType | None = None
    _api_client: AbstractCodexFFAPIClient

    @abstractmethod
    async def _perform_update(self) -> None:
        pass

    async def _update(self) -> None:
        """Update FFmpeg build."""
        self._log.info('Updating FFmpeg binaries from %s', self.TYPE)
        if await self._needs_update():
            await self._perform_update()
        else:
            self._log.info('FFmpeg binaries are up-to-date, nothing to update')

    async def _needs_update(self) -> bool:
        """Check if ffbinaries need to be updated."""
        if self._settings.force or not self._all_ffbinaries_exist():
            return True

        latest_version, local_version = await asyncio.gather(
            self._api_client.get_latest_version(), self._get_local_version()
        )
        self._log.info(
            'Local FFmpeg version "%s", latest version "%s"',
            local_version,
            latest_version,
        )
        if latest_version != local_version:
            self._log.info(
                'Local FFmpeg build version %s needs update to %s',
                local_version,
                latest_version,
            )
            return True
        return False

    def _all_ffbinaries_exist(self) -> bool:
        """Check whether all FFmpeg binaries exist on disk."""
        files = self._settings.destination.iterdir()
        return len(set(files) & RequiredFfbinaryType.choices()) == len(
            RequiredFfbinaryType
        )

    async def _get_local_version(self) -> str | None:
        """Get local FFmpeg build numerical build version."""
        bin_path = self._settings.destination / RequiredFfbinaryType.FFMPEG
        try:
            stdout = await get_stdout(
                cmd=(bin_path.as_posix(), CMD_FFMPEG_VERSION_ARG), log=self._log
            )
            self._log.debug('Local FFmpeg build version:\n\n%s', stdout)
        except FileNotFoundError:
            self._log.warning(
                'Local FFmpeg build not found, will proceed with download'
            )
            return None
        except OSError as err:
            self._log.warning('Error getting local FFmpeg build version: "%s"', err)
            return None

        match = re.match(FFMPEG_NUM_REGEX, stdout)
        if not match:
            self._log.warning(
                'Error getting local FFmpeg build version using regex "%s"',
                FFMPEG_NUM_REGEX,
            )
            return None
        return match.group(1)
