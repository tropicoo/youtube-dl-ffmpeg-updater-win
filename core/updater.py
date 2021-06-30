"""Updater module."""

import asyncio
import logging
import os
from argparse import Namespace

from core.exceptions import UpdaterError
from core.managers import TaskManager


class Updater:
    """Main updater class."""

    def __init__(self, settings: Namespace):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)
        self._settings = settings
        self._task_manager = TaskManager(self._settings)

    async def run(self) -> None:
        """Start update tasks."""
        self._log.info('Starting%s update', ' force' if self._settings.force else '')
        self._check_path_existence(self._settings.destination)
        await asyncio.gather(*self._task_manager.create_tasks(), return_exceptions=True)
        self._log.info('%spdate finished', 'Force u' if self._settings.force else 'U')

    def _check_path_existence(self, path: str) -> None:
        """Check if destination path exists and is a directory."""
        if not os.path.exists(path):
            self._log.info('Creating non-existing directory %s', path)
            os.makedirs(path)
        elif not os.path.isdir(path):
            raise UpdaterError(f'{path} is not a directory')
