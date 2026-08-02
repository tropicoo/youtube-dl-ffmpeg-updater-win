from typing import Final

from ffmpeg_updater_win.app.clients.abstract import BaseApiClient
from ffmpeg_updater_win.app.clients.codex_ffmpeg.client import (
    BaseCodexFFAPIClient,
    CodexFFAPIClient,
    CodexFFGithubApiClient,
)
from ffmpeg_updater_win.app.clients.ytdl import YTDLApiClient
from ffmpeg_updater_win.app.enums import CodexSourceType
from ffmpeg_updater_win.app.models.config import UpdaterConfig
from ffmpeg_updater_win.app.tasks.abstract import BaseUpdaterTask
from ffmpeg_updater_win.app.tasks.codex import CodexFfmpegUpdaterTask
from ffmpeg_updater_win.app.tasks.youtube_dl import YTDLUpdaterTask

CODEX_SOURCE_API_MAP: Final[dict[CodexSourceType, type[BaseCodexFFAPIClient]]] = {
    CodexSourceType.CODEX: CodexFFAPIClient,
    CodexSourceType.GITHUB: CodexFFGithubApiClient,
}


def get_api_cls(
    settings: UpdaterConfig, updater_task_cls: type[BaseUpdaterTask]
) -> type[BaseApiClient]:
    if issubclass(updater_task_cls, CodexFfmpegUpdaterTask):
        return CODEX_SOURCE_API_MAP[settings.codex_source]
    if issubclass(updater_task_cls, YTDLUpdaterTask):
        return YTDLApiClient
    raise ValueError(f'Unknown updater task class "{updater_task_cls}"')
