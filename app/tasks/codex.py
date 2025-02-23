from typing import Literal

from app.enums import FFSourceType, WinPlatformType
from app.extractor import ZipStreamExtractor
from app.tasks.abstract import AbstractFFmpegUpdaterTask


class CodexFfmpegUpdaterTask(AbstractFFmpegUpdaterTask):
    TYPE: Literal[FFSourceType.CODEX] = FFSourceType.CODEX

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._stream_extractor = ZipStreamExtractor(settings=self._settings)

    async def _perform_update(self) -> None:
        if self._settings.platform is not WinPlatformType.WIN64:
            self._log.warning('Codex FFmpeg builds are only 64bit')
        await self._stream_extractor.process_zip_stream(
            self._api_client.download_latest_version()
        )
