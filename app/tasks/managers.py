"""Managers Module."""

import logging
from asyncio import Task
from typing import ClassVar

from app.clients.abstract import AbstractApiClient
from app.enums import UpdaterComponentType
from app.mappings import get_api_cls
from app.settings import Settings
from app.tasks.abstract import AbstractUpdaterTask
from app.tasks.codex import CodexFfmpegUpdaterTask
from app.utils import create_task


class TaskManager:
    TASKS: ClassVar[
        dict[UpdaterComponentType, tuple[type[AbstractUpdaterTask], ...]]
    ] = {
        # UpdaterComponentType.ALL: (CodexFfmpegUpdaterTask, YTDLUpdaterTask),
        UpdaterComponentType.FFMPEG: (CodexFfmpegUpdaterTask,),
        # UpdaterComponentType.YTDL: (YTDLUpdaterTask,),
    }

    def __init__(self, settings: Settings) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing "%s"', self.__class__.__name__)
        self._settings = settings

    def create_tasks(self) -> list[Task]:
        tasks: list[Task] = []
        for task_cls in self.TASKS[self._settings.component]:
            tasks.append(
                create_task(
                    task_cls(
                        settings=self._settings,
                        api_client=self._create_api_client(task_cls=task_cls),
                    ).run(),
                    logger=self._log,
                    task_name=task_cls.__name__,
                    exception_message='Task %s raised an exception',
                    exception_message_args=(task_cls.__name__,),
                )
            )
        return tasks

    def _create_api_client(
        self, task_cls: type[AbstractUpdaterTask]
    ) -> AbstractApiClient:
        return get_api_cls(settings=self._settings, updater_task_cls=task_cls)()
