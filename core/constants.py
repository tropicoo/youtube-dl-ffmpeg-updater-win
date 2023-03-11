"""Constants Module."""
from core.enums import LogLevel, WinPlatform

LOG_FORMAT_DEBUG = (
    '%(asctime)s %(module)-11s %(name)-25s %(funcName)-23s %(levelname)-8s %(message)s'
)
LOG_FORMAT_INFO = '%(name)-25s %(levelname)-8s %(message)s'

LOG_MAP = {
    LogLevel.ERROR.value: LOG_FORMAT_INFO,
    LogLevel.WARNING.value: LOG_FORMAT_INFO,
    LogLevel.INFO.value: LOG_FORMAT_INFO,
    LogLevel.DEBUG.value: LOG_FORMAT_DEBUG,
}

DEF_EXTRACT_PATH = r'C:\youtube-dl'

EXE_YTDL = 'youtube-dl.exe'
URL_YTDL = f'https://youtube-dl.org/downloads/latest/{EXE_YTDL}'

FFMPEG_NUM_REGEX = r'(([0-9]+\.?)+)'

PLATFORMS = {
    WinPlatform.WIN32: {'endpoint': 'windows-32', 'type': 0},
    WinPlatform.WIN64: {'endpoint': 'windows-64', 'type': 6},
}

CMD_YOUTUBE_DL_UPDATE = '{bin_path} --update'
CMD_FFMPEG_VERSION = '{bin_path} -version'

CHUNK_SIZE = 1024 * 1024

EXIT_OK = 0
EXIT_ERROR = 1
