"""Processes Module."""

import logging
import multiprocessing
import os
import re
import subprocess

from ffbinaries import FFBinariesAPIClient

from core.api import YouTubeDLAPIClient
from core.const import (CHUNK_SIZE, CMD_FFMPEG_VERSION, CMD_YOUTUBE_DL_UPDATE,
                        EXE_YTDL, FFMPEG_NUM_REGEX, PLATFORMS,
                        REQUIRED_FFBINARIES)
from core.extractor import ZipExtractor
from core.log import init_logging
from core.utils import init_shared_manager, response_to_zip


class BaseUpdaterProcess(multiprocessing.Process):
    """Base Updater Process Class."""

    def __init__(self, api_client, settings):
        super().__init__()
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)
        self._api = api_client
        self._settings = settings

    def run(self):
        """Main Process Run Method."""
        init_logging(self._settings.log_level)
        self._update()

    def _update(self):
        """Update Method."""
        raise NotImplementedError


class YTDLUpdaterProcess(BaseUpdaterProcess):
    """youtube-dl Updater Process Class."""

    def __init__(self, settings):
        super().__init__(api_client=YouTubeDLAPIClient(settings.log_level),
                         settings=settings)

    def _update(self):
        """Update youtube-dl."""
        self._log.info('Updating %s', EXE_YTDL)

        if self._settings.force:
            self._update_from_web()
            return

        try:
            self._update_via_subprocess()
        except FileNotFoundError:
            self._log.info('Local %s build not found, downloading from web',
                           EXE_YTDL)
            self._update_from_web()

    def _update_from_web(self):
        """Update youtube-dl from the web."""
        stream_obj = self._api.download_latest_version()
        with open(os.path.join(self._settings.destination, EXE_YTDL),
                  'wb') as f_out:
            for chunk in stream_obj.iter_content(chunk_size=CHUNK_SIZE):
                f_out.write(chunk)

        self._print_version()

    def _print_version(self):
        cmd = os.path.join(self._settings.destination, EXE_YTDL + ' --version')
        version = subprocess.check_output(cmd, text=True).strip()
        self._log.info(f'youtube-dl updated to version {version}')

    def _update_via_subprocess(self):
        """Update youtube-dl by subprocess call."""
        stdout = subprocess.check_output(CMD_YOUTUBE_DL_UPDATE.format(
            bin_path=os.path.join(self._settings.destination, EXE_YTDL)),
            text=True).strip()
        self._log.info(stdout)


class FFCompUpdaterProcess(BaseUpdaterProcess):
    """ffmpeg Component Updater Process Class."""

    def __init__(self, api_client, settings, queue):
        super().__init__(api_client=api_client, settings=settings)
        self._queue = queue
        self._extractor = ZipExtractor()

    def _update(self):
        while self._queue.qsize() > 0:
            component_res = self._api.download_latest_version(
                platform=PLATFORMS[self._settings.platform]['endpoint'],
                component=self._queue.get())
            self._extractor.extract(response_to_zip(component_res),
                                    dest=self._settings.destination)


class BaseFFUpdaterProcess(BaseUpdaterProcess):

    def __init__(self, api_client, settings):
        super().__init__(api_client=api_client, settings=settings)

    def _update(self):
        """Update ffmpeg build."""
        self._log.info('Updating ffbinaries')
        if self._need_update():
            self._perform_update()
        else:
            self._log.info('ffbinaries are up-to-date, nothing to update')

    def _perform_update(self):
        raise NotImplementedError

    def _need_update(self):
        """Check if ffbinaries need to be updated."""
        if self._settings.force or not self._all_ffbinaries_exist():
            return True
        latest_version = self._api.get_latest_version()
        local_version = self._get_local_version()
        if latest_version != local_version:
            self._log.info('Local ffmpeg build version %s needs update to %s',
                           local_version, latest_version)
            return True
        return False

    def _all_ffbinaries_exist(self):
        files = os.listdir(self._settings.destination)
        return len(set(files) & set(REQUIRED_FFBINARIES)) \
               == len(REQUIRED_FFBINARIES)

    def _get_local_version(self):
        """Get local ffmpeg build numerical build version."""
        ffmpeg_ver = None
        try:
            ffmpeg_ver = subprocess.check_output(CMD_FFMPEG_VERSION.format(
                bin_path=os.path.join(self._settings.destination,
                                      REQUIRED_FFBINARIES[0])),
                text=True).splitlines()[0]
            ffmpeg_ver = re.search(FFMPEG_NUM_REGEX, ffmpeg_ver).group()
        except FileNotFoundError:
            self._log.warning('Local ffmpeg build not found, will proceed '
                              'with download')
        except OSError as err:
            self._log.warning('Error getting local ffmpeg build version: %s',
                              err)
        return ffmpeg_ver


class FFUpdaterProcess(BaseFFUpdaterProcess):
    """ffmpeg Updater Process Class."""

    def __init__(self, settings):
        manager = init_shared_manager((FFBinariesAPIClient,))
        super().__init__(api_client=manager.FFBinariesAPIClient(
            use_caching=True, log_init=(init_logging, settings.log_level)),
            settings=settings)
        self._spawned = []

    def _perform_update(self):
        queue = multiprocessing.Manager().Queue()
        for comp in map(lambda x: x.rsplit('.', 1)[0], REQUIRED_FFBINARIES):
            queue.put(comp)

        for i in range(len(REQUIRED_FFBINARIES)):
            proc = FFCompUpdaterProcess(api_client=self._api,
                                        queue=queue,
                                        settings=self._settings)
            proc.start()
            self._spawned.append(proc)

        for proc in self._spawned:
            proc.join()
