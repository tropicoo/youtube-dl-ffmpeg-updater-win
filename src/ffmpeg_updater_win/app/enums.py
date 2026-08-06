"""Enums module."""

from enum import IntEnum, StrEnum


class BaseStrChoiceEnum(StrEnum):
    @classmethod
    def choices(cls) -> frozenset[str]:
        return frozenset(member.value for member in cls)


class LogLevelType(IntEnum):
    """Log Level Name to Verbosity level."""

    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3


class ExitCodeType(IntEnum):
    EXIT_OK = 0
    EXIT_ERROR = 1


class UpdaterComponentType(BaseStrChoiceEnum):
    FFMPEG = 'ffmpeg'


class WinPlatformType(BaseStrChoiceEnum):
    """Windows platform types."""

    WIN32 = 'win32'
    WIN64 = 'win64'


class FFSourceType(BaseStrChoiceEnum):
    CODEX = 'codex'


class CodexReleaseType(BaseStrChoiceEnum):
    GIT = 'git'
    RELEASE = 'release'
    TOOLS = 'tools'


class CodexBuildType(BaseStrChoiceEnum):
    ESSENTIALS = 'essentials'
    FULL = 'full'


class RequiredFfbinaryType(BaseStrChoiceEnum):
    FFMPEG = 'ffmpeg.exe'
    FFPROBE = 'ffprobe.exe'
    FFPLAY = 'ffplay.exe'


class CodexSourceType(BaseStrChoiceEnum):
    GITHUB = 'github'
    CODEX = 'codex'


class CodexAPIPathType(BaseStrChoiceEnum):
    CHANGELOG_COUNTER = 'changelog-counter'

    LATEST_GIT_VER = 'git-version'
    LATEST_RELEASE_VER = 'release-version'
    LATEST_TOOLS_VER = 'tools-version'

    LAST_BUILD_UPDATE = 'last-build-update'
    NEXT_BUILD_UPDATE = 'next-build-update'


class CodexArchExtensionType(BaseStrChoiceEnum):
    ZIP = 'zip'
    SEVEN_ZIP = '7z'
