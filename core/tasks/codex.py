from argparse import Namespace

from core.clients.codexffmpeg import CodexFFAPIClient
from core.constants import FFSource, WinPlatform
from core.extractor import ZipExtractor
from core.tasks.abstract import AbstractFFmpegUpdaterTask
from core.utils import response_to_zip


class CodexFfmpegUpdaterTask(AbstractFFmpegUpdaterTask):

    type = FFSource.CODEX

    def __init__(self, settings: Namespace):
        super().__init__(api_client=CodexFFAPIClient(), settings=settings)
        self._extractor = ZipExtractor()

    async def _perform_update(self) -> None:
        if self._settings.platform != WinPlatform.WIN64:
            self._log.warning('Codex FFmpeg builds are only 64bit')

        response = await self._api.download_latest_version()
        await self._extractor.extract(response_to_zip(response), dest=self._settings.destination)
