"""Managers Module."""

import logging

from core.const import FFSource
from core.procs import (FFUpdaterProcess, FFUpdaterProcessZeranoe,
                        YTDLUpdaterProcess)


class UpdaterProcessManager:
    """Updater Process Manager Class.

    Intended to start update processes.
    """

    _ffmpeg_proc_map = {FFSource.FFBINARIES: FFUpdaterProcess,
                        FFSource.ZERANOE: FFUpdaterProcessZeranoe}

    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)
        self._procs = [YTDLUpdaterProcess]

        self._jobs = []

    def start_processes(self, settings):
        """Start Updater Processes."""
        self._procs.append(self._ffmpeg_proc_map[settings.ff_src])

        for i in range(len(self._procs)):
            proc = self._procs[i](settings)
            self._log.debug('Starting %s', proc)
            proc.start()
            self._jobs.append(proc)

        for job in self._jobs:
            job.join()
