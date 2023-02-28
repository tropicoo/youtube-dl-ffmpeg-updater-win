from argparse import Namespace

from core.clients.codexffmpeg import CodexFFAPIClient
from core.constants import FFSource, WinPlatform
from core.extractor import ZipStreamExtractor
from core.tasks.abstract import AbstractFFmpegUpdaterTask


class CodexFfmpegUpdaterTask(AbstractFFmpegUpdaterTask):
    type = FFSource.CODEX

    def __init__(self, settings: Namespace) -> None:
        super().__init__(api_client=CodexFFAPIClient(), settings=settings)
        self._stream_extractor = ZipStreamExtractor(self._settings)

    async def _perform_update(self) -> None:
        if self._settings.platform != WinPlatform.WIN64:
            self._log.warning('Codex FFmpeg builds are only 64bit')
        await self._stream_extractor.process_zip_stream(
            self._api.download_latest_version()
        )
