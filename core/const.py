"""Constants Module."""


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
FFBINARIES_API = 'http://ffbinaries.com/api/v1/version/latest'
FFMPEG_NUM_REGEX = r'(([0-9]+\.?)+)'

PLATFORMS = {'x32': 'windows-32',
             'x64': 'windows-64'}

CMD_YOUTUBE_DL_UPDATE = '{bin_path} --update'
CMD_FFMPEG_VERSION = '{bin_path} -version'

CHUNKS_SIZE = 8192

EXIT_OK = 0
EXIT_ERROR = 1
