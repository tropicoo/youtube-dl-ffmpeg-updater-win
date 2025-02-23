import logging
from pathlib import Path

from app.utils import get_stdout


class FFmpegBinValidationTask:
    def __init__(self) -> None:
        self._log = logging.getLogger(self.__class__.__name__)

    async def validate(self, bin_path: Path) -> None:
        _ = await get_stdout(
            cmd=(bin_path.as_posix(), '-version'), log=self._log, raise_on_stderr=True
        )
        self._log.info('%s successfully validated', bin_path)
