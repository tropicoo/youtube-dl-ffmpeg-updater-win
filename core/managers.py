"""Managers Module."""

import logging

from core.procs import FFUpdaterProcess, YTDLUpdaterProcess


class UpdaterProcessManager:
    """Updater Process Manager Class."""

    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)
        self._procs = (FFUpdaterProcess, YTDLUpdaterProcess)
        self._jobs = []

    def start_processes(self, settings):
        """Start Updater Processes."""
        for i in range(len(self._procs)):
            proc = self._procs[i](settings)
            self._log.info('Starting %s', proc)
            proc.start()
            self._jobs.append(proc)

        for job in self._jobs:
            job.join()
