import logging
import os
import shutil
from zipfile import ZipFile

from aiofiles.os import wrap  # noqa


class ZipExtractTask:

    def __init__(self, zip_file: ZipFile, context: dict):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)

        self._zip_file = zip_file
        self._ctx = context
        self._copyfileobj = wrap(shutil.copyfileobj)

    async def extract(self) -> None:
        with self._zip_file.open(self._ctx['member']) as src, \
                open(os.path.join(self._ctx['dest'], self._ctx['filename']), 'wb') as target:
            self._log.info('[%s] Extract %s to %s', self._zip_file.filename, src.name, target.name)
            await self._copyfileobj(src, target)
