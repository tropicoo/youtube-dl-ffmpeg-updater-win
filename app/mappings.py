from typing import Final

from app.clients.abstract import BaseApiClient
from app.clients.codex_ffmpeg.client import (
    BaseCodexFFAPIClient,
    CodexFFAPIClient,
    CodexFFGithubApiClient,
)
from app.clients.ytdl import YTDLApiClient
from app.enums import CodexSourceType
from app.settings import Settings
from app.tasks.abstract import BaseUpdaterTask
from app.tasks.codex import CodexFfmpegUpdaterTask
from app.tasks.youtube_dl import YTDLUpdaterTask

CODEX_SOURCE_API_MAP: Final[dict[CodexSourceType, type[BaseCodexFFAPIClient]]] = {
    CodexSourceType.CODEX: CodexFFAPIClient,
    CodexSourceType.GITHUB: CodexFFGithubApiClient,
}


def get_api_cls(
    settings: Settings, updater_task_cls: type[BaseUpdaterTask]
) -> type[BaseApiClient]:
    if issubclass(updater_task_cls, CodexFfmpegUpdaterTask):
        return CODEX_SOURCE_API_MAP[settings.codex_source]
    if issubclass(updater_task_cls, YTDLUpdaterTask):
        return YTDLApiClient
    raise ValueError(f'Unknown updater task class "{updater_task_cls}"')
