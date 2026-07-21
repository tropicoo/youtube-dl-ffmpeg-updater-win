"""Updater module."""

import asyncio
import logging

from app.exceptions import UpdaterError
from app.settings import Settings
from app.tasks.managers import TaskManager
from app.version import __version__


class Updater:
    """Main updater class."""

    def __init__(self, settings: Settings) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.info(
            'Initializing "%s" version %s', self.__class__.__name__, __version__
        )
        self._settings = settings
        self._task_manager = TaskManager(settings=self._settings)

    async def run(self) -> None:
        """Start update tasks."""
        self._log.info('Starting%s update', ' force' if self._settings.force else '')
        self._check_destination_path_existence()
        await asyncio.gather(*self._task_manager.create_tasks(), return_exceptions=True)
        self._log.info('%spdate finished', 'Force u' if self._settings.force else 'U')

    def _check_destination_path_existence(self) -> None:
        """Check if destination path exists and is a directory."""
        path = self._settings.destination
        if not path.exists():
            self._log.info('Creating destination directory "%s"', path)
            path.mkdir(parents=True)
            return

        if not path.is_dir():
            raise UpdaterError(f'{path} is not a directory')
