"""Constants Module."""

from pathlib import WindowsPath
from typing import Final

from core.enums import LogLevel

LOG_FORMAT_DEBUG: Final[str] = (
    '%(asctime)s %(module)-11s %(name)-25s %(funcName)-23s %(levelname)-8s %(message)s'
)
LOG_FORMAT_INFO: Final[str] = '%(name)-25s %(levelname)-8s %(message)s'

LOG_MAP: Final[dict[LogLevel, str]] = {
    LogLevel.ERROR: LOG_FORMAT_INFO,
    LogLevel.WARNING: LOG_FORMAT_INFO,
    LogLevel.INFO: LOG_FORMAT_INFO,
    LogLevel.DEBUG: LOG_FORMAT_DEBUG,
}

DEF_EXTRACT_PATH: Final[WindowsPath] = WindowsPath(r'C:\youtube-dl')

EXE_YTDL: Final[str] = 'youtube-dl.exe'
URL_YTDL: Final[str] = f'https://youtube-dl.org/downloads/latest/{EXE_YTDL}'

FFMPEG_NUM_REGEX: Final[str] = r'(([0-9]+\.?)+)'

CMD_YOUTUBE_DL_UPDATE: Final[str] = '{bin_path} --update'
CMD_FFMPEG_VERSION: Final[str] = '{bin_path} -version'

CHUNK_SIZE: Final[int] = 1024 * 1024

EXIT_OK: Final[int] = 0
EXIT_ERROR: Final[int] = 1
