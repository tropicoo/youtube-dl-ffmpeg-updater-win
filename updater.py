"""youtube-dl and ffmpeg packages updater for Windows OS."""

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
FFMPEG_REGEX = r'ffmpeg-[0-9\.]+-win64-static\.zip'

EXTRACT_PATH = r'C:\youtube-dl'
EXTRACT_FILES = ('ffmpeg.exe', 'ffprobe.exe', 'ffplay.exe')

CMD_YOUTUBE_DL_UPDATE = f'{os.path.join(EXTRACT_PATH, EXE_YTDL)} -U'
CMD_FFMPEG_VERSION = f'{os.path.join(EXTRACT_PATH, EXTRACT_FILES[0])} -version'

EXIT_OK = 0
EXIT_ERROR = 1


class _HTTPMethods:
    __slots__ = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self):
        for method in self.__slots__:
            setattr(self, method, method)


HTTP = _HTTPMethods()


class BaseUpdaterProcess(multiprocessing.Process):
    def __init__(self):
        super().__init__()
        self._log = logging.getLogger(self.__class__.__name__)

    def run(self):
        self._update()

    def _update(self):
        raise NotImplementedError

    def _request(self, url, method=HTTP.GET):
        return requests.request(method=method, url=url)


class YTDLUpdaterProcess(BaseUpdaterProcess):
    def _update(self):
        self._log.info('Updating %s', EXE_YTDL)
        try:
            self._update_through_subprocess()
        except FileNotFoundError:
            self._log.info('local %s build not found, downloading from web',
                           EXE_YTDL)
            self._update_through_web()

    def _update_through_web(self):
        yt_exe = self._request(url=URL_YTDL).content
        with open(os.path.join(EXTRACT_PATH, EXE_YTDL), 'wb') as f_out:
            f_out.write(yt_exe)

    def _update_through_subprocess(self):
        stdout = subprocess.check_output(CMD_YOUTUBE_DL_UPDATE,
                                         text=True).strip()
        self._log.info(stdout)


class FFMPEGUpdaterProcess(BaseUpdaterProcess):
    def _update(self):
        if not os.path.exists(EXTRACT_PATH):
            os.makedirs(EXTRACT_PATH)

        latest_ffmpeg_zip = self._get_latest_build()
        zip_file = ZipFile(BytesIO(latest_ffmpeg_zip))
        self._extract_zip(zip_file)

    def _extract_zip(self, zip_file):
        for member in zip_file.namelist():
            filename = os.path.basename(member)
            if not filename or filename not in EXTRACT_FILES:
                continue

            with zip_file.open(member) as source, \
                    open(os.path.join(EXTRACT_PATH, filename), 'wb') as target:
                shutil.copyfileobj(source, target)

    def _get_latest_build(self):
        html = self._request(url=URL_FFMPEG).text
        # Get last element since already sorted by ascending order.
        latest_ver = [x.group() for x in re.finditer(FFMPEG_REGEX, html)][-1]
        return self._request(
            url=posixpath.join(URL_FFMPEG, latest_ver)).content

    def _get_local_version(self):
        ffmpeg_ver = None
        try:
            ffmpeg_ver = subprocess.check_output(CMD_FFMPEG_VERSION,
                                                 text=True).splitlines()[0]
            ffmpeg_ver = re.search(r'([0-9]+\.?)+', ffmpeg_ver)
        except FileNotFoundError:
            self._log.info('local ffmpeg build not found, will proceed '
                           'with download')
        return ffmpeg_ver


class UpdaterProcessManager:
    def __init__(self):
        self._procs = (FFMPEGUpdaterProcess(), YTDLUpdaterProcess())

    def start_update_processes(self):
        jobs = []
        for i in range(len(self._procs)):
            proc = self._procs[i]
            proc.start()
            jobs.append(proc)

        for job in jobs:
            job.join()


class Updater:
    def __init__(self):
        self._manager = UpdaterProcessManager()

    def start_update(self):
        self._manager.start_update_processes()


def main():
    updater = Updater()
    updater.start_update()


if __name__ == '__main__':
    log_format = '%(asctime)s - %(name)s - %(levelname)s - [%(threadName)s] - [%(funcName)s,%(lineno)d] - %(message)s'
    logging.basicConfig(format=log_format, level=logging.DEBUG,
                        stream=sys.stdout)
    multiprocessing.log_to_stderr(logging.DEBUG)
    main()
