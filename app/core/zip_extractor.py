"""Zip Extractor module."""

import asyncio
import logging
from collections.abc import AsyncGenerator
from pathlib import Path

import aiofiles

from app.enums import RequiredFfbinaryType
from app.settings import Settings
from app.tasks.validation import FFmpegBinValidationTask
from app.utils import create_task


class ZipStreamExtractor:
    """Stream FFmpeg binaries chunk extractor."""

    def __init__(self, settings: Settings) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing "%s"', self.__class__.__name__)
        self._settings = settings
        self._validation_tasks = []

    async def process_zip_stream(
        self,
        stream_generator: AsyncGenerator[
            tuple[bytes, int, AsyncGenerator[bytes, None]], None
        ],
    ) -> None:
        """Process stream chunks, write FFmpeg binaries on the fly and fire up validation tasks."""
        ffbinaries = RequiredFfbinaryType.choices()
        written_files_count, ffbinaries_count = 0, len(ffbinaries)
        async for member_, _file_size, unzipped_chunks in stream_generator:
            member = member_.decode()
            filename = Path(member).name
            if filename not in ffbinaries:
                self._log.debug('Skip %s', member)
                async for _ in unzipped_chunks:
                    # Go through chunks for unneeded files and throw them out.
                    pass
                continue

            await self._write_file(filename, unzipped_chunks)
            written_files_count += 1
            if written_files_count == ffbinaries_count:
                break

        await asyncio.gather(*self._validation_tasks)
        self._log.info('All ffbinaries updated, zip stream process done')

    async def _write_file(self, filename: str, unzipped_chunks) -> None:  # noqa: ANN001
        """Write unzipped chunks into file."""
        file_path = self._settings.destination / filename
        self._log.debug('Write file %s', file_path)
        async with aiofiles.open(file_path, 'wb') as fd_out:
            async for chunk in unzipped_chunks:
                await fd_out.write(chunk)
        self._start_validation_task(file_path)

    def _start_validation_task(self, file_path: Path) -> None:
        """Spawn exe validation task."""
        self._validation_tasks.append(
            create_task(
                FFmpegBinValidationTask().validate(file_path),
                task_name=f'Validation<{file_path}>',
                logger=self._log,
                exception_message='Task %s raised an exception',
                exception_message_args=(FFmpegBinValidationTask.__name__,),
            )
        )
