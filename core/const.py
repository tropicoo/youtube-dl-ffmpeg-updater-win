"""Constants Module."""

LOG_FORMAT_DEBUG = '%(asctime)s %(module)-9s %(processName)-24s %(name)-21s %(funcName)-22s %(levelname)-8s %(message)s'
LOG_FORMAT_INFO = '%(name)-21s %(message)s'

LOG_MAP = {0: ('ERROR', LOG_FORMAT_INFO),
           1: ('WARNING', LOG_FORMAT_INFO),
           2: ('INFO', LOG_FORMAT_INFO),
           3: ('DEBUG', LOG_FORMAT_DEBUG)}


class _FfmpegLinkingType:
    """ffmpeg linking types."""

    STATIC = 'static'
    SHARED = 'shared'
    DEV = 'dev'


class _HTTPMethods:
    """HTTP Methods Class."""

    GET = 'get'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'


class _WinPlatform:
    """Windows platform types."""

    WIN32 = 'win32'
    WIN64 = 'win64'


class FFReleaseChannel:
    DEV = 'dev'
    RELEASE = 'release'


class FFSource:
    FFBINARIES = 'ffbinaries'
    ZERANOE = 'zeranoe'


FfmpegLinkingType = _FfmpegLinkingType()
Http = _HTTPMethods()
WinPlatform = _WinPlatform()

DEF_EXTRACT_PATH = r'C:\youtube-dl'

EXE_YTDL = 'youtube-dl.exe'
URL_YTDL = f'https://yt-dl.org/latest/{EXE_YTDL}'

REQUIRED_FFBINARIES = ('ffmpeg.exe', 'ffprobe.exe', 'ffplay.exe')
FFMPEG_NUM_REGEX = r'(([0-9]+\.?)+)'

PLATFORMS = {WinPlatform.WIN32: {'endpoint': 'windows-32', 'type': 0},
             WinPlatform.WIN64: {'endpoint': 'windows-64', 'type': 6}}

CMD_YOUTUBE_DL_UPDATE = '{bin_path} --update'
CMD_FFMPEG_VERSION = '{bin_path} -version'

CHUNK_SIZE = 8192

EXIT_OK = 0
EXIT_ERROR = 1
