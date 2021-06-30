"""Constants Module."""

import enum

LOG_FORMAT_DEBUG = '%(asctime)s %(module)-11s %(name)-25s %(funcName)-23s %(levelname)-8s %(message)s'
LOG_FORMAT_INFO = '%(name)-25s %(levelname)-8s %(message)s'

LOG_MAP = {
    0: ('ERROR', LOG_FORMAT_INFO),
    1: ('WARNING', LOG_FORMAT_INFO),
    2: ('INFO', LOG_FORMAT_INFO),
    3: ('DEBUG', LOG_FORMAT_DEBUG),
}


class FfmpegLinkingType:
    """FFmpeg linking types."""

    STATIC = 'static'
    SHARED = 'shared'
    DEV = 'dev'


class HTTPMethods:
    """HTTP Methods Class."""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


Http = HTTPMethods


class UpdaterComponent:
    ALL = 'all'
    FFMPEG = 'ffmpeg'
    YTDL = 'ytdl'


class WinPlatform:
    """Windows platform types."""

    WIN32 = 'win32'
    WIN64 = 'win64'


class FFReleaseChannel:
    DEV = 'dev'
    RELEASE = 'release'


class FFSource:
    CODEX = 'codex'
    FFBINARIES = 'ffbinaries'


class CodexReleaseType:
    GIT = 'git'
    RELEASE = 'release'
    TOOLS = 'tools'


class CodexBuildType:
    ESSENTIALS = 'essentials'
    FULL = 'full'


DEF_EXTRACT_PATH = r'C:\youtube-dl'

EXE_YTDL = 'youtube-dl.exe'
URL_YTDL = f'https://youtube-dl.org/downloads/latest/{EXE_YTDL}'


@enum.unique
class RequiredFfbinaries(enum.Enum):
    FFMPEG = 'ffmpeg.exe'
    FFPROBE = 'ffprobe.exe'
    FFPLAY = 'ffplay.exe'

    @classmethod
    def choices(cls):
        return frozenset(member.value for member in cls)


FFMPEG_NUM_REGEX = r'(([0-9]+\.?)+)'

PLATFORMS = {
    WinPlatform.WIN32: {'endpoint': 'windows-32', 'type': 0},
    WinPlatform.WIN64: {'endpoint': 'windows-64', 'type': 6}
}

CMD_YOUTUBE_DL_UPDATE = '{bin_path} --update'
CMD_FFMPEG_VERSION = '{bin_path} -version'

CHUNK_SIZE = 1024 * 1024

EXIT_OK = 0
EXIT_ERROR = 1
