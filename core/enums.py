"""Constants Module."""

from enum import Enum, IntEnum, StrEnum


class BaseChoiceEnum(Enum):
    @classmethod
    def choices(cls) -> frozenset[str]:
        return frozenset(member.value for member in cls)


class LogLevel(IntEnum):
    """Log Level Name to Verbosity level."""

    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3


class FfmpegLinkingType(BaseChoiceEnum, StrEnum):
    """FFmpeg linking types."""

    STATIC = 'static'
    SHARED = 'shared'
    DEV = 'dev'


class HTTPMethods(BaseChoiceEnum, StrEnum):
    """HTTP Methods Class."""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


class UpdaterComponent(BaseChoiceEnum, StrEnum):
    ALL = 'all'
    FFMPEG = 'ffmpeg'
    YTDL = 'ytdl'


class WinPlatform(BaseChoiceEnum, StrEnum):
    """Windows platform types."""

    WIN32 = 'win32'
    WIN64 = 'win64'


class FFReleaseChannel(BaseChoiceEnum, StrEnum):
    DEV = 'dev'
    RELEASE = 'release'


class FFSource(BaseChoiceEnum, StrEnum):
    CODEX = 'codex'
    FFBINARIES = 'ffbinaries'


class CodexReleaseType(BaseChoiceEnum, StrEnum):
    GIT = 'git'
    RELEASE = 'release'
    TOOLS = 'tools'


class CodexBuildType(BaseChoiceEnum, StrEnum):
    ESSENTIALS = 'essentials'
    FULL = 'full'


class RequiredFfbinaries(BaseChoiceEnum, StrEnum):
    FFMPEG = 'ffmpeg.exe'
    FFPROBE = 'ffprobe.exe'
    FFPLAY = 'ffplay.exe'


class CodexSource(BaseChoiceEnum, StrEnum):
    GITHUB = 'github'
    CODEX = 'codex'
