"""Constants Module."""

from enum import IntEnum, StrEnum, unique


@unique
class LogLevel(IntEnum):
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3


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


@unique
class RequiredFfbinaries(StrEnum):
    FFMPEG = 'ffmpeg.exe'
    FFPROBE = 'ffprobe.exe'
    FFPLAY = 'ffplay.exe'

    @classmethod
    def choices(cls) -> frozenset[str]:
        return frozenset(member.value for member in cls)


class CodexSource(StrEnum):
    GITHUB = 'github'
    CODEX = 'codex'
