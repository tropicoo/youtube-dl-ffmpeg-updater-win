"""Updater module."""

import asyncio
import logging
import os

from core.exceptions import UpdaterError
from core.managers import TaskManager
from core.settings import Settings
from core.version import __version__


class Updater:
    """Main updater class."""

    def __init__(self, settings: Settings) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.info(
            'Initializing %s version %s', self.__class__.__name__, __version__
        )
        self._settings = settings
        self._task_manager = TaskManager(self._settings)

    async def run(self) -> None:
        """Start update tasks."""
        self._log.info('Starting%s update', ' force' if self._settings.force else '')
        self._check_path_existence()
        await asyncio.gather(*self._task_manager.create_tasks(), return_exceptions=True)
        self._log.info('%spdate finished', 'Force u' if self._settings.force else 'U')

    def _check_path_existence(self) -> None:
        """Check if destination path exists and is a directory."""
        path = self._settings.destination
        if not os.path.exists(path):
            self._log.info('Creating non-existing directory %s', path)
            os.makedirs(path)
        elif not os.path.isdir(path):
            raise UpdaterError(f'{path} is not a directory')
