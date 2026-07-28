"""Constants module."""

from pathlib import Path
from typing import Final

from app.enums import LogLevel

WINDOWS_PLATFORM: Final[str] = 'Windows'

LOG_FORMAT_DEBUG: Final[str] = (
    '%(asctime)s %(module)-15s %(name)-25s %(funcName)-24s %(levelname)-8s %(message)s'
)
LOG_FORMAT_INFO: Final[str] = '%(name)-25s %(levelname)-8s %(message)s'

LOG_MAP: Final[dict[LogLevel, str]] = {
    LogLevel.ERROR: LOG_FORMAT_INFO,
    LogLevel.WARNING: LOG_FORMAT_INFO,
    LogLevel.INFO: LOG_FORMAT_INFO,
    LogLevel.DEBUG: LOG_FORMAT_DEBUG,
}

DEF_EXTRACT_PATH: Final[Path] = Path(r'C:\youtube-dl')

EXE_YTDL: Final[str] = 'youtube-dl.exe'
URL_YTDL: Final[str] = f'https://youtube-dl.org/downloads/latest/{EXE_YTDL}'

FFMPEG_NUM_REGEX: Final[str] = r'^ffmpeg\s+version\s+([\d\.]+)'

CMD_YOUTUBE_DL_UPDATE: Final[str] = '--update'
CMD_FFMPEG_VERSION_ARG: Final[str] = '-version'

CHUNK_SIZE: Final[int] = 1024 * 1024

EXIT_OK: Final[int] = 0
EXIT_ERROR: Final[int] = 1
