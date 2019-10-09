"""Processes Module."""

import logging
import multiprocessing
import os
import re
import subprocess
from io import BytesIO
from zipfile import ZipFile

from core.api import YouTubeDLAPIClient, FFBinariesAPIClient
from core.const import (EXE_YTDL, CMD_YOUTUBE_DL_UPDATE, CMD_FFMPEG_VERSION,
                        REQUIRED_FFBINARIES, CHUNKS_SIZE, FFMPEG_NUM_REGEX)
from core.extractor import ZipExtractor
from core.log import init_logging
from core.utils import init_shared_manager


class BaseUpdaterProcess(multiprocessing.Process):
    """Base Updater Process Class."""

    def __init__(self, dest, api_client, platform, force=False):
        super().__init__()
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)
        self._api = api_client
        self._destination = dest
        self._platform = platform
        self._force = force

    def run(self):
        """Main Process Run Method."""
        init_logging()
        self._update()

    def _update(self):
        """Update Method."""
        raise NotImplementedError


class YTDLUpdaterProcess(BaseUpdaterProcess):
    """youtube-dl Updater Process Class."""

    def __init__(self, dest, platform, force):
        super().__init__(dest=dest,
                         platform=platform,
                         api_client=YouTubeDLAPIClient(),
                         force=force)

    def _update(self):
        """Update youtube-dl."""
        self._log.info('Updating %s', EXE_YTDL)

        if self._force:
            self._update_through_web()
            return

        try:
            self._update_through_subprocess()
        except FileNotFoundError:
            self._log.info('Local %s build not found, downloading from web',
                           EXE_YTDL)
            self._update_through_web()

    def _update_through_web(self):
        """Update youtube-dl through the web."""
        stream_obj = self._api.download_latest_version()
        with open(os.path.join(self._destination, EXE_YTDL), 'wb') as f_out:
            for chunk in stream_obj.iter_content(chunk_size=CHUNKS_SIZE):
                f_out.write(chunk)

    def _update_through_subprocess(self):
        """Update youtube-dl by subprocess call."""
        stdout = subprocess.check_output(CMD_YOUTUBE_DL_UPDATE.format(
            bin_path=os.path.join(self._destination, EXE_YTDL)), text=True).strip()
        self._log.info(stdout)


class FFComponentUpdaterProcess(BaseUpdaterProcess):
    """ffmpeg Component Updater Process Class."""

    def __init__(self, api_client, queue, dest, platform):
        super().__init__(dest=dest,
                         platform=platform,
                         api_client=api_client)
        self._queue = queue
        self._extractor = ZipExtractor()

    def _update(self):
        while self._queue.qsize() > 0:
            component_obj = self._api.download_latest_version(
                platform=self._platform,
                component=self._queue.get())
            zip_archive = ZipFile(BytesIO(component_obj))
            self._extractor.extract(zip_archive, dest=self._destination)


class FFUpdaterProcess(BaseUpdaterProcess):
    """ffmpeg Updater Process Class."""

    def __init__(self, dest, platform, force):
        manager = init_shared_manager((FFBinariesAPIClient,))
        super().__init__(dest=dest,
                         platform=platform,
                         api_client=manager.FFBinariesAPIClient(),
                         force=force)
        self._spawned = []

    def _update(self):
        """Update ffmpeg build."""
        self._log.info('Updating ffbinaries')
        if self._need_update():
            queue = multiprocessing.Manager().Queue()
            for comp in map(lambda x: x.rsplit('.', 1)[0], REQUIRED_FFBINARIES):
                queue.put(comp)

            for i in range(len(REQUIRED_FFBINARIES)):
                proc = FFComponentUpdaterProcess(api_client=self._api,
                                                 queue=queue,
                                                 dest=self._destination,
                                                 platform=self._platform)
                proc.start()
                self._spawned.append(proc)

            for proc in self._spawned:
                proc.join()
        else:
            self._log.info('ffbinaries are up-to-date, nothing to update')

    def _need_update(self):
        """Check if ffbinaries need to be updated."""
        if self._force or not self._all_ffbinaries_exist():
            return True
        latest_version = self._api.get_latest_version()
        local_version = self._get_local_version()
        if latest_version != local_version:
            self._log.info('Local ffmpeg build version %s needs update to %s',
                           local_version, latest_version)
            return True
        return False

    def _all_ffbinaries_exist(self):
        files = os.listdir(self._destination)
        return len(set(REQUIRED_FFBINARIES) & set(files)) \
               == len(REQUIRED_FFBINARIES)

    def _get_local_version(self):
        """Get local ffmpeg build numerical build version."""
        ffmpeg_ver = None
        try:
            ffmpeg_ver = subprocess.check_output(CMD_FFMPEG_VERSION.format(
                bin_path=os.path.join(self._destination, REQUIRED_FFBINARIES[0])),
                                                 text=True).splitlines()[0]
            ffmpeg_ver = re.search(FFMPEG_NUM_REGEX, ffmpeg_ver).group()
        except FileNotFoundError:
            self._log.info('Local ffmpeg build not found, will proceed '
                           'with download')
        except OSError as err:
            self._log.warning('Error getting local ffmpeg build version: %s',
                              err)
        return ffmpeg_ver
