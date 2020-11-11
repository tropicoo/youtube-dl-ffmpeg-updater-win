"""youtube-dl and ffmpeg packages updater for Windows OS."""

import argparse

from core.const import DEF_EXTRACT_PATH, FFSource, LOG_MAP, WinPlatform
from core.log import init_logging
from core.updater import Updater


def parse_args():
    parser = argparse.ArgumentParser(
        description='youtube-dl & ffmpeg binaries updater for windows os')
    parser.add_argument('-d', '--destination', default=DEF_EXTRACT_PATH,
                        action='store', dest='destination',
                        help=f'youtube-dl directory path, default {DEF_EXTRACT_PATH}')
    parser.add_argument('-p', '--platform', default=WinPlatform.WIN32,
                        action='store', dest='platform',
                        choices=(WinPlatform.WIN32, WinPlatform.WIN64),
                        help='ffmpeg binaries os platform, default win32')
    parser.add_argument('-f', '--force', default=False, action='store_true',
                        dest='force', help='force update')
    parser.add_argument('-ff-src', '--ffmpeg-source', default=FFSource.FFBINARIES,
                        action='store', dest='ff_src', help='ffbinaries source',
                        choices=(FFSource.FFBINARIES,))
    parser.add_argument('-v', '--verbose', nargs='?', const=2, default=2,
                        action='store', dest='log_level', type=int,
                        help='log level 0-3, default 2', choices=LOG_MAP.keys())
    return parser.parse_args()


def main():
    """Main function."""
    args = parse_args()
    init_logging(args.log_level)

    updater = Updater(settings=args)
    updater.run()


if __name__ == '__main__':
    main()
