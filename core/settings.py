from dataclasses import dataclass
from pathlib import Path

from core.enums import CodexSource, FFSource, LogLevel, UpdaterComponent


@dataclass
class Settings:
    component: UpdaterComponent
    destination: Path
    platform: str
    force: bool
    ffmpeg_source: FFSource
    codex_source: CodexSource
    verbose: LogLevel
