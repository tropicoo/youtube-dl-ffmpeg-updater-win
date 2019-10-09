"""Zip Extractor module."""

import logging
import os
import shutil

from core.const import REQUIRED_FFBINARIES


class ZipExtractor:
    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)

    def extract(self, zip_file, dest):
        """Extract downloaded ffbinary zip archive."""
        for member in zip_file.namelist():
            filename = os.path.basename(member)
            if not filename or filename not in REQUIRED_FFBINARIES:
                self._log.debug('Skipping %s', member)
                continue

            with zip_file.open(member) as source, \
                    open(os.path.join(dest, filename), 'wb') as target:
                self._log.info('Extracting %s to %s', source.name, target.name)
                shutil.copyfileobj(source, target)
