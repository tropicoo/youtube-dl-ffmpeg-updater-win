from pathlib import Path

from pydantic import BaseModel, ConfigDict

from app.enums import (
    CodexSourceType,
    FFSourceType,
    LogLevel,
    UpdaterComponentType,
    WinPlatformType,
)


class Settings(BaseModel):
    model_config = ConfigDict(
        strict=True, frozen=True, extra='forbid', arbitrary_types_allowed=True
    )

    component: UpdaterComponentType
    destination: Path
    platform: WinPlatformType
    force: bool
    ffmpeg_source: FFSourceType
    codex_source: CodexSourceType
    verbose: LogLevel
