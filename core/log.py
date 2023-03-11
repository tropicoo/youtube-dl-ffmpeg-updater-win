"""Logging Module."""

import logging

from core.constants import LOG_MAP
from core.enums import LogLevel


def init_logging(
    log_level: int, suppress_asyncio: bool = True, suppress_urllib3: bool = True
) -> None:
    """Init logging function. Used for new processes that don't have
    configured `root` logger.
    """
    logging.basicConfig(
        format=LOG_MAP[log_level],
        level=LogLevel(log_level).name,
        datefmt='%Y-%m-%d %H:%M:%S',
        force=True,
    )
    if suppress_asyncio:
        logging.getLogger('asyncio').setLevel(logging.WARNING)
    if suppress_urllib3:
        logging.getLogger('urllib3').setLevel(logging.WARNING)
