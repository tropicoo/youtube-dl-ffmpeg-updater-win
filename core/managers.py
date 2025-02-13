"""Managers Module."""

import logging
from asyncio import Task

from tasks.abstract import AbstractUpdaterTask

from core.enums import UpdaterComponentType
from core.settings import Settings
from core.tasks.codex import CodexFfmpegUpdaterTask
from core.tasks.youtube_dl import YTDLUpdaterTask
from core.utils import create_task


class TaskManager:
    _TASKS: dict[UpdaterComponentType, tuple[type[AbstractUpdaterTask], ...]] = {
        UpdaterComponentType.ALL: (CodexFfmpegUpdaterTask, YTDLUpdaterTask),
        UpdaterComponentType.FFMPEG: (CodexFfmpegUpdaterTask,),
        UpdaterComponentType.YTDL: (YTDLUpdaterTask,),
    }

    def __init__(self, settings: Settings) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)
        self._settings = settings

    def create_tasks(self) -> list[Task]:
        tasks = []
        for task_cls in self._TASKS[self._settings.component]:
            tasks.append(
                create_task(
                    task_cls(self._settings).run(),
                    logger=self._log,
                    task_name=task_cls.__name__,
                    exception_message='Task %s raised an exception',
                    exception_message_args=(task_cls.__name__,),
                )
            )
        return tasks
