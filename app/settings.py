from dataclasses import dataclass
from pathlib import Path

from app.enums import (
    CodexSourceType,
    FFSourceType,
    LogLevel,
    UpdaterComponentType,
    WinPlatformType,
)


@dataclass
class Settings:
    component: UpdaterComponentType
    destination: Path
    platform: WinPlatformType
    force: bool
    ffmpeg_source: FFSourceType
    codex_source: CodexSourceType
    verbose: LogLevel
