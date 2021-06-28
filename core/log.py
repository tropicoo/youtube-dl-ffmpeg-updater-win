"""Logging Module."""

import logging

from core.constants import LOG_MAP


def init_logging(log_level) -> None:
    """Init logging function. Used for new processes that don't have
    configured `root` logger.
    """
    level, log_format = LOG_MAP[log_level]
    logging.basicConfig(format=log_format, level=level)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('asyncio').setLevel(logging.WARNING)
