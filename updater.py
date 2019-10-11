"""youtube-dl and ffmpeg packages updater for Windows OS."""

import argparse
import logging
import logging.config
import logging.handlers
import os

from core.const import DEF_EXTRACT_PATH, PLATFORMS, LOG_MAP
from core.exceptions import UpdaterException
from core.log import init_logging
from core.managers import UpdaterProcessManager


class Updater:
    """Updater Class."""

    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)
        self._manager = UpdaterProcessManager()

    def run(self, settings):
        """Start Update."""
        if settings.force:
            self._log.info('Performing force update')
        self._log.info('Starting update')
        self._check_path_existence(settings.destination)
        self._manager.start_processes(settings)
        self._log.info('Update finished')

    def _check_path_existence(self, path):
        """Check if destination path exists and is directory."""
        if not os.path.exists(path):
            self._log.info('Destination path %s does not exist, creating', path)
            os.makedirs(path)
        elif not os.path.isdir(path):
            raise UpdaterException(f'{path} is not a directory')


def parse_args():
    parser = argparse.ArgumentParser(
        description='youtube-dl & ffmpeg binaries updater for windows os')
    parser.add_argument('-d', '--destination', default=DEF_EXTRACT_PATH,
                        action='store', dest='destination',
                        help=f'youtube-dl directory path, default {DEF_EXTRACT_PATH}')
    parser.add_argument('-p', '--platform', default='x32', action='store',
                        dest='platform', choices=PLATFORMS.keys(),
                        help='ffmpeg binaries os platform, default x32')
    parser.add_argument('-f', '--force', default=False, action='store_true',
                        dest='force', help='force update')
    parser.add_argument('-v', '--verbose', nargs='?', const=2, default=2,
                        action='store', dest='log_level', type=int,
                        help='log level 0-3, default 2', choices=LOG_MAP.keys())
    return parser.parse_args()


def main():
    """Main function."""
    args = parse_args()
    init_logging(args.log_level)

    updater = Updater()
    updater.run(settings=args)


if __name__ == '__main__':
    main()
