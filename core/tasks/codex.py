from typing import ClassVar, Literal

from clients.codexffmpeg import (
    AbstractCodexFFAPIClient,
    CodexFFAPIClient,
    CodexFFGithubApiClient,
)

from core.enums import CodexSourceType, FFSourceType, WinPlatformType
from core.extractor import ZipStreamExtractor
from core.settings import Settings
from core.tasks.abstract import AbstractFFmpegUpdaterTask


class CodexFfmpegUpdaterTask(AbstractFFmpegUpdaterTask):
    TYPE: Literal[FFSourceType.CODEX] = FFSourceType.CODEX

    _API_CLIENT_CLS_MAP: ClassVar[
        dict[CodexSourceType, type[AbstractCodexFFAPIClient]]
    ] = {
        CodexSourceType.CODEX: CodexFFAPIClient,
        CodexSourceType.GITHUB: CodexFFGithubApiClient,
    }

    def __init__(self, settings: Settings) -> None:
        api_client_cls = self._API_CLIENT_CLS_MAP[settings.codex_source]
        super().__init__(api_client=api_client_cls(), settings=settings)
        self._stream_extractor = ZipStreamExtractor(self._settings)

    async def _perform_update(self) -> None:
        if self._settings.platform != WinPlatformType.WIN64:
            self._log.warning('Codex FFmpeg builds are only 64bit')
        await self._stream_extractor.process_zip_stream(
            self._api_client.download_latest_version()
        )
