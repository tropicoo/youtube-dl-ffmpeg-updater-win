"""Updater module."""

import logging
import os

from core.exceptions import UpdaterException
from core.managers import UpdaterProcessManager


class Updater:
    """Updater Class."""

    def __init__(self, settings):
        self._log = logging.getLogger(self.__class__.__name__)
        self._settings = settings
        self._log.debug('Initializing %r', self)
        self._manager = UpdaterProcessManager(settings)

    def run(self):
        """Start Update."""
        self._log.info('Starting%s update', ' force' if self._settings.force else '')
        self._check_path_existence(self._settings.destination)
        self._manager.start_processes()
        self._log.info('Update finished')

    def _check_path_existence(self, path):
        """Check if destination path exists and is a directory."""
        if not os.path.exists(path):
            self._log.info('Destination path %s does not exist, creating', path)
            os.makedirs(path)
        elif not os.path.isdir(path):
            raise UpdaterException(f'{path} is not a directory')
