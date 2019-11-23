"""Constants Module."""

LOG_FORMAT_DEBUG = '%(asctime)s %(module)-9s %(processName)-24s %(name)-21s %(funcName)-22s %(levelname)-8s %(message)s'
LOG_FORMAT_INFO = '%(name)-21s %(message)s'

LOG_MAP = {0: ('ERROR', LOG_FORMAT_INFO),
           1: ('WARNING', LOG_FORMAT_INFO),
           2: ('INFO', LOG_FORMAT_INFO),
           3: ('DEBUG', LOG_FORMAT_DEBUG)}


class _HTTPMethods:
    """HTTP Methods Class."""
    __slots__ = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self):
        for method in self.__slots__:
            setattr(self, method, method)


HTTP = _HTTPMethods()

DEF_EXTRACT_PATH = r'C:\youtube-dl'

EXE_YTDL = 'youtube-dl.exe'
URL_YTDL = f'https://yt-dl.org/latest/{EXE_YTDL}'

REQUIRED_FFBINARIES = ('ffmpeg.exe', 'ffprobe.exe', 'ffplay.exe')
FFMPEG_NUM_REGEX = r'(([0-9]+\.?)+)'

PLATFORMS = {'x32': {'endpoint': 'windows-32',
                     'type': 0},
             'x64': {'endpoint': 'windows-64',
                     'type': 6}}

CMD_YOUTUBE_DL_UPDATE = '{bin_path} --update'
CMD_FFMPEG_VERSION = '{bin_path} -version'

CHUNKS_SIZE = 8192

EXIT_OK = 0
EXIT_ERROR = 1
