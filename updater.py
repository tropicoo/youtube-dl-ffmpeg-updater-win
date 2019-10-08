"""youtube-dl and ffmpeg packages updater for Windows OS."""

import argparse
import logging
import logging.config
import logging.handlers
import os

from core.const import DEF_EXTRACT_PATH, PLATFORMS
from core.exceptions import UpdaterException
from core.log import init_logging
from core.managers import UpdaterProcessManager


class Updater:
    """Updater Class."""

    def __init__(self, dest, platform):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)
        self._manager = UpdaterProcessManager()
        self._destination = dest
        self._platform = platform

    def run(self, force=False):
        """Start Update."""
        self._log.info('Starting update')
        self._check_path_existence()
        if force:
            self._log.info('Performing force update')
        self._manager.start_update_processes(dest=self._destination,
                                             platform=self._platform,
                                             force=force)
        self._log.info('Update finished')

    def _check_path_existence(self):
        """Check if destination path exists and is directory."""
        if not os.path.exists(self._destination):
            self._log.info('Destination path %s does not exist, creating',
                           self._destination)
            os.makedirs(self._destination)
        elif not os.path.isdir(self._destination):
            raise UpdaterException(f'{self._destination} is not a directory')


def parse_args():
    parser = argparse.ArgumentParser(
        description='youtube-dl & ffmpeg binaries updater for windows')
    parser.add_argument('-d', '--destination', default=DEF_EXTRACT_PATH,
                        action='store', dest='extract_path',
                        help='youtube-dl directory path')
    parser.add_argument('-p', '--platform', default='x32', action='store',
                        dest='platform', choices=PLATFORMS.keys(),
                        help='ffmpeg binaries os platform')
    parser.add_argument('-f', '--force', default=False, action='store_true',
                        dest='force', help='force update')
    return parser.parse_args()


def main():
    """Main function."""
    init_logging()
    args = parse_args()
    updater = Updater(dest=args.extract_path,
                      platform=PLATFORMS[args.platform])
    updater.run(force=args.force)


if __name__ == '__main__':
    main()
