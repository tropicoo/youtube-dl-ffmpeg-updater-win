import asyncio
import logging

from core.argparser import parse_args
from core.log import init_logging
from core.updater import Updater
from core.version import __version__


async def main() -> None:
    args = parse_args()
    init_logging(args.log_level)
    logger = logging.getLogger(__name__)
    logger.info('Starting Updater %s', __version__)
    try:
        updater = Updater(settings=args)
        await updater.run()
    finally:
        logger.info('Exiting Updater %s', __version__)


if __name__ == '__main__':
    # Not using "asyncio.run(main())" due to bug https://github.com/aio-libs/aiohttp/issues/4324
    asyncio.get_event_loop().run_until_complete(main())
