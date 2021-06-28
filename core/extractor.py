"""Zip Extractor module."""
import abc
import asyncio
import logging
import os
from zipfile import ZipFile

from core.constants import REQUIRED_FFBINARIES
from core.exceptions import NoFileToExtractError
from core.tasks.extract import ZipExtractTask


class AbstractZipExtractor(abc.ABC):
    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)

    @abc.abstractmethod
    async def extract(self, zip_file: ZipFile, dest: str):
        pass

    @abc.abstractmethod
    def _get_extract_coros(self, zip_file: ZipFile, dest: str):
        pass


class ZipExtractor(AbstractZipExtractor):

    async def extract(self, zip_file: ZipFile, dest: str):
        """Extract downloaded ffmpeg binaries zip archive."""
        extract_coroutines = self._get_extract_coros(zip_file, dest)
        if not extract_coroutines:
            err_msg = 'No files found to extract'
            self._log.error(err_msg)
            raise NoFileToExtractError(err_msg)
        await asyncio.gather(*extract_coroutines)

    def _get_extract_coros(self, zip_file: ZipFile, dest: str) -> list:
        extract_coroutines = []
        for member in zip_file.namelist():
            filename = os.path.basename(member)
            if not filename or filename not in REQUIRED_FFBINARIES:
                self._log.debug('[%s] Skip %s', zip_file.filename, member)
                continue

            context = {'member': member, 'dest': dest, 'filename': filename}
            extract_coroutines.append(ZipExtractTask(zip_file, context).extract())
        return extract_coroutines
