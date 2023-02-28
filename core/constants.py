"""Constants Module."""

from enum import IntEnum, StrEnum, unique

LOG_FORMAT_DEBUG = (
    '%(asctime)s %(module)-11s %(name)-25s %(funcName)-23s %(levelname)-8s %(message)s'
)
LOG_FORMAT_INFO = '%(name)-25s %(levelname)-8s %(message)s'


@unique
class LogLevel(IntEnum):
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3


LOG_MAP = {
    LogLevel.ERROR.value: LOG_FORMAT_INFO,
    LogLevel.WARNING.value: LOG_FORMAT_INFO,
    LogLevel.INFO.value: LOG_FORMAT_INFO,
    LogLevel.DEBUG.value: LOG_FORMAT_DEBUG,
}


class FfmpegLinkingType(StrEnum):
    """FFmpeg linking types."""

    STATIC = 'static'
    SHARED = 'shared'
    DEV = 'dev'


class HTTPMethods(StrEnum):
    """HTTP Methods Class."""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


class UpdaterComponent(StrEnum):
    ALL = 'all'
    FFMPEG = 'ffmpeg'
    YTDL = 'ytdl'


class WinPlatform(StrEnum):
    """Windows platform types."""

    WIN32 = 'win32'
    WIN64 = 'win64'


class FFReleaseChannel(StrEnum):
    DEV = 'dev'
    RELEASE = 'release'


class FFSource(StrEnum):
    CODEX = 'codex'
    FFBINARIES = 'ffbinaries'


class CodexReleaseType(StrEnum):
    GIT = 'git'
    RELEASE = 'release'
    TOOLS = 'tools'


class CodexBuildType(StrEnum):
    ESSENTIALS = 'essentials'
    FULL = 'full'


DEF_EXTRACT_PATH = r'C:\youtube-dl'

EXE_YTDL = 'youtube-dl.exe'
URL_YTDL = f'https://youtube-dl.org/downloads/latest/{EXE_YTDL}'


@unique
class RequiredFfbinaries(StrEnum):
    FFMPEG = 'ffmpeg.exe'
    FFPROBE = 'ffprobe.exe'
    FFPLAY = 'ffplay.exe'

    @classmethod
    def choices(cls) -> frozenset[str]:
        return frozenset(member.value for member in cls)


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
