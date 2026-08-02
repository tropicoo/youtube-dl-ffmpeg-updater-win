from pathlib import Path

from pydantic import BaseModel, ConfigDict

from ffmpeg_updater_win.app.enums import (
    CodexSourceType,
    FFSourceType,
    LogLevelType,
    UpdaterComponentType,
    WinPlatformType,
)


class Settings(BaseModel):
    model_config = ConfigDict(
        strict=True,
        frozen=True,
        extra='forbid',
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
    )

    component: UpdaterComponentType
    destination: Path
    platform: WinPlatformType
    force: bool
    ffmpeg_source: FFSourceType
    codex_source: CodexSourceType
    verbose: LogLevelType
