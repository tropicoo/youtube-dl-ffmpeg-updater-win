import asyncio

from argparser import parse_args
from core.log import init_logging
from core.updater import Updater


async def main() -> None:
    args = parse_args()
    init_logging(args.log_level)
    updater = Updater(settings=args)
    await updater.run()


if __name__ == '__main__':
    # Not using "asyncio.run(main())" due to bug https://github.com/aio-libs/aiohttp/issues/4324
    asyncio.get_event_loop().run_until_complete(main())
