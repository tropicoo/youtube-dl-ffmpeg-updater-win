from dataclasses import dataclass
from pathlib import Path

from core.enums import CodexSourceType, FFSourceType, LogLevel, UpdaterComponentType


@dataclass
class Settings:
    component: UpdaterComponentType
    destination: Path
    platform: str
    force: bool
    ffmpeg_source: FFSourceType
    codex_source: CodexSourceType
    verbose: LogLevel
