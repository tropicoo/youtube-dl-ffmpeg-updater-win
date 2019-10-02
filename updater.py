"""youtube-dl and ffmpeg packages updater for Windows OS.

TODO: multiprocessing logging (currently not working).
TODO: argparse (platform version, stable/nightly, static/shared/dev)
"""

import argparse
import logging
import multiprocessing
import os
import posixpath
import re
import shutil
import subprocess
import sys
from io import BytesIO
from zipfile import ZipFile

import requests

EXE_YTDL = 'youtube-dl.exe'
URL_YTDL = f'https://yt-dl.org/latest/{EXE_YTDL}'
URL_FFMPEG = 'https://ffmpeg.zeranoe.com/builds/win64/static/'
FFMPEG_NUM_REGEX = r'(([0-9]+\.?)+)'
FFMPEG_BUILD_REGEX = fr'ffmpeg-{FFMPEG_NUM_REGEX}-win64-static\.zip'

EXTRACT_PATH = r'C:\youtube-dl'
EXTRACT_FILES = ('ffmpeg.exe', 'ffprobe.exe', 'ffplay.exe')

CMD_YOUTUBE_DL_UPDATE = f'{os.path.join(EXTRACT_PATH, EXE_YTDL)} --update'
CMD_FFMPEG_VERSION = f'{os.path.join(EXTRACT_PATH, EXTRACT_FILES[0])} -version'

EXIT_OK = 0
EXIT_ERROR = 1


class UpdaterException(Exception):
    """Updater Base Exception Class."""
    pass


class HTTPMethods:
    """HTTP Methods Class."""
    __slots__ = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self):
        for method in self.__slots__:
            setattr(self, method, method)


HTTP = HTTPMethods()


class BaseUpdaterProcess(multiprocessing.Process):
    """Base Updater Process Class."""

    def __init__(self):
        super().__init__()
        self._log = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Main Process Run Method."""
        self._update()

    def _update(self):
        """Update Method."""
        raise NotImplementedError

    def _request(self, url, method=HTTP.GET):
        """General Request Method."""
        return requests.request(method=method, url=url)


class YTDLUpdaterProcess(BaseUpdaterProcess):
    """youtube-dl Updater Process Class."""

    def _update(self):
        """Update youtube-dl."""
        self._log.info('Updating %s', EXE_YTDL)
        try:
            self._update_through_subprocess()
        except FileNotFoundError:
            self._log.info('local %s build not found, downloading from web',
                           EXE_YTDL)
            self._update_through_web()

    def _update_through_web(self):
        """Update youtube-dl through the web."""
        ytdl_exe = self._request(url=URL_YTDL).content
        with open(os.path.join(EXTRACT_PATH, EXE_YTDL), 'wb') as f_out:
            f_out.write(ytdl_exe)

    def _update_through_subprocess(self):
        """Update youtube-dl by subprocess call."""
        stdout = subprocess.check_output(CMD_YOUTUBE_DL_UPDATE,
                                         text=True).strip()
        self._log.info(stdout)


class FFMPEGUpdaterProcess(BaseUpdaterProcess):
    """fmpeg Updater Process Class."""

    def __init__(self):
        super().__init__()
        self._latest_build_name = None

    def _update(self):
        """Update ffmpeg build."""
        if self._needs_update():
            latest_ffmpeg_zip = self._get_latest_build()
            self._extract_zip(latest_ffmpeg_zip)

    def _needs_update(self):
        """Check if ffmpeg needs to be updated."""
        latest_version = self._get_latest_version()
        local_version = self._get_local_version()
        if not local_version:
            return True

        if latest_version == local_version:
            return False
        return True

    def _get_latest_version(self):
        """Get latest ffmpeg numerical build version."""
        html = self._request(url=URL_FFMPEG).text
        match = None

        for match in re.finditer(FFMPEG_BUILD_REGEX, html):
            # Remember the last match since build names are already sorted
            # by ascending order in the html.
            pass

        if not match:
            raise UpdaterException('Failed to get ffmpeg latest version')

        self._latest_build_name = match.group()
        return match.group(1)

    def _extract_zip(self, zip_file):
        """Extract downloaded ffmpeg build zip archive."""
        for member in zip_file.namelist():
            filename = os.path.basename(member)
            if not filename or filename not in EXTRACT_FILES:
                continue

            with zip_file.open(member) as source, \
                    open(os.path.join(EXTRACT_PATH, filename), 'wb') as target:
                shutil.copyfileobj(source, target)

    def _get_latest_build(self):
        """Download latest ffmpeg build zip archive."""
        ffmpeg_zip = self._request(
            url=posixpath.join(URL_FFMPEG, self._latest_build_name)).content
        return ZipFile(BytesIO(ffmpeg_zip))

    def _get_local_version(self):
        """Get local ffmpeg build numerical build version."""
        ffmpeg_ver = None
        try:
            ffmpeg_ver = subprocess.check_output(CMD_FFMPEG_VERSION,
                                                 text=True).splitlines()[0]
            ffmpeg_ver = re.search(FFMPEG_NUM_REGEX, ffmpeg_ver).group()
        except FileNotFoundError:
            self._log.info('local ffmpeg build not found, will proceed '
                           'with download')
        return ffmpeg_ver


class UpdaterProcessManager:
    """Updater Process Manager Class."""

    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.info('Initializing Updater Process Manager')
        self._procs = (FFMPEGUpdaterProcess(), YTDLUpdaterProcess())
        self._jobs = []

    def start_update_processes(self):
        """Start Updater Processes."""
        for i in range(len(self._procs)):
            proc = self._procs[i]
            self._log.info('Starting %s', proc)
            proc.start()
            self._jobs.append(proc)

        for job in self._jobs:
            job.join()


class Updater:
    """Updater Class."""

    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.info('Initializing Updater')
        self._manager = UpdaterProcessManager()

    def start_update(self):
        """Start Update."""
        self._log.info('Starting update')
        self._check_path_existence()
        self._manager.start_update_processes()

    def _check_path_existence(self):
        """Check if destination path exists and is directory."""
        if not os.path.exists(EXTRACT_PATH):
            self._log.info('Destination path %s does not exist, creating',
                           EXTRACT_PATH)
            os.makedirs(EXTRACT_PATH)
        elif not os.path.isdir(EXTRACT_PATH):
            raise UpdaterException(f'{EXTRACT_PATH} is not a directory')


def main():
    """Main function."""
    updater = Updater()
    updater.start_update()


if __name__ == '__main__':
    log_format = '%(asctime)s - %(name)s - %(levelname)s - [%(threadName)s] - [%(funcName)s,%(lineno)d] - %(message)s'
    logging.basicConfig(format=log_format, level=logging.DEBUG,
                        stream=sys.stdout)
    main()
