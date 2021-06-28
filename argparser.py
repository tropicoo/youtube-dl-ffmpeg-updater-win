import argparse

from core.constants import DEF_EXTRACT_PATH, LOG_MAP, FFSource, UpdaterComponent, WinPlatform


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='youtube-dl & ffmpeg binaries updater for windows os')
    parser.add_argument('-c', '--component', default=UpdaterComponent.ALL,
                        action='store', dest='component',
                        choices={UpdaterComponent.ALL, UpdaterComponent.FFMPEG,
                                 UpdaterComponent.YTDL},
                        help=f'updater components to update, default {UpdaterComponent.ALL}')
    parser.add_argument('-d', '--destination', default=DEF_EXTRACT_PATH,
                        action='store', dest='destination',
                        help=f'youtube-dl directory path, default {DEF_EXTRACT_PATH}')
    parser.add_argument('-p', '--platform', default=WinPlatform.WIN64,
                        action='store', dest='platform',
                        choices={WinPlatform.WIN32, WinPlatform.WIN64},
                        help=f'ffmpeg binaries os platform, default {WinPlatform.WIN64}')
    parser.add_argument('-f', '--force', default=False, action='store_true',
                        dest='force', help='perform force update')
    parser.add_argument('-ff-src', '--ffmpeg-source',
                        default=FFSource.CODEX,
                        action='store', dest='ff_src',
                        help='ffmpeg binaries source, currently supported only from codex',
                        choices={FFSource.CODEX})
    parser.add_argument('-v', '--verbose', nargs='?', const=2, default=2,
                        action='store', dest='log_level', type=int,
                        help='log level 0-3, default 2',
                        choices=LOG_MAP.keys())
    return parser.parse_args()
