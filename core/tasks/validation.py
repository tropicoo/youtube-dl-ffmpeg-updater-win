import logging
from abc import ABC

from core.utils import get_stdout


class FFmpegBinValidationTask(ABC):
    def __init__(self) -> None:
        self._log = logging.getLogger(self.__class__.__name__)

    async def validate(self, bin_path: str) -> None:
        _ = await get_stdout(bin_path + ' -version', self._log, raise_on_stderr=True)
        self._log.info('%s successfully validated', bin_path)
