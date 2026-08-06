from typing import Final

from ffmpeg_updater_win.app.constants import APP_VERSION
from ffmpeg_updater_win.main import main

__version__: Final[str] = APP_VERSION

__all__: Final[str] = ['__version__', 'main']
