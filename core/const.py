"""Constants Module."""

LOG_FORMAT_DEBUG = '%(asctime)s %(module)-9s %(processName)-24s %(name)-21s %(funcName)-22s %(levelname)-8s %(message)s'
LOG_FORMAT_INFO = '%(name)-21s %(message)s'

LOG_MAP = {0: ('ERROR', LOG_FORMAT_INFO),
           1: ('WARNING', LOG_FORMAT_INFO),
           2: ('INFO', LOG_FORMAT_INFO),
           3: ('DEBUG', LOG_FORMAT_DEBUG)}


class _FfmpegLinkingType:
    """ffmpeg linking types."""

    __slots__ = ('STATIC', 'SHARED', 'DEV')

    def __init__(self):
        for method in self.__slots__:
            setattr(self, method, method.lower())


class _HTTPMethods:
    """HTTP Methods Class."""

    __slots__ = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self):
        for method in self.__slots__:
            setattr(self, method, method)


class _WinPlatform:
    """Windows platform types."""

    __slots__ = ('WIN32', 'WIN64')

    def __init__(self):
        for method in self.__slots__:
            setattr(self, method, method.lower())


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

URL_ZERANOE = 'https://ffmpeg.zeranoe.com'
URL_ZERANOE_BUILDS = f'{URL_ZERANOE}/builds'
URL_ZERANOE_BUILDS_JSON = f'{URL_ZERANOE_BUILDS}/builds.json'
FFMPEG_FILE_ZERANOE_PATTERN = 'ffmpeg-{build_version}-{platform}-{linking}.zip'
URL_ZERANOE_DOWNLOAD = f'{URL_ZERANOE_BUILDS}/{{platform}}/{{linking}}/{{filename}}'

REQUIRED_FFBINARIES = ('ffmpeg.exe', 'ffprobe.exe', 'ffplay.exe')
FFMPEG_NUM_REGEX = r'(([0-9]+\.?)+)'

PLATFORMS = {WinPlatform.WIN32: {'endpoint': 'windows-32', 'type': 0},
             WinPlatform.WIN64: {'endpoint': 'windows-64', 'type': 6}}

CMD_YOUTUBE_DL_UPDATE = '{bin_path} --update'
CMD_FFMPEG_VERSION = '{bin_path} -version'

CHUNK_SIZE = 8192

EXIT_OK = 0
EXIT_ERROR = 1
