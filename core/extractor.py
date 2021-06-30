"""Zip Extractor module."""

import logging
import os

import aiofiles

from core.constants import RequiredFfbinaries


class ZipStreamExtractor:
    """Stream FFmpeg binaries chunk extractor."""

    def __init__(self, settings):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)
        self._settings = settings

    async def process_zip_stream(self, stream_generator):
        """Process stream chunks and write found FFmpeg binaries on the fly."""
        ffbinaries = RequiredFfbinaries.choices()
        written_files_count, ffbinaries_count = 0, len(ffbinaries)
        async for member, file_size, unzipped_chunks in stream_generator:
            member = member.decode()
            filename = os.path.basename(member)

            if filename not in ffbinaries:
                self._log.debug('Skip %s', member)
                async for _ in unzipped_chunks:
                    # Go through chunks for unneeded files in zip-archive and throw them out.
                    pass
                continue

            file_path = os.path.join(self._settings.destination, filename)
            self._log.debug('Write file %s', file_path)
            async with aiofiles.open(file_path, 'wb') as fd_out:
                async for chunk in unzipped_chunks:
                    await fd_out.write(chunk)

            written_files_count += 1
            if written_files_count == ffbinaries_count:
                self._log.debug('All ffbinaries updated, done zip stream process')
                break
