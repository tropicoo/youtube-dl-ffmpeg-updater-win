"""Managers Module."""

import logging

from core.const import FFSource
from core.procs import FFUpdaterProcess, YTDLUpdaterProcess


class UpdaterProcessManager:
    """Updater Process Manager Class.

    Intended to start update processes.
    """

    _ffmpeg_proc_map = {FFSource.FFBINARIES: FFUpdaterProcess}

    def __init__(self, settings):
        self._log = logging.getLogger(self.__class__.__name__)
        self._settings = settings
        self._log.debug('Initializing %r', self)
        self._procs = [YTDLUpdaterProcess]

        self._jobs = []

    def start_processes(self):
        """Start Updater Processes."""
        self._procs.append(self._ffmpeg_proc_map[self._settings.ff_src])

        for i in range(len(self._procs)):
            proc = self._procs[i](self._settings)
            self._log.debug('Starting %s', proc)
            proc.start()
            self._jobs.append(proc)

        for job in self._jobs:
            job.join()
