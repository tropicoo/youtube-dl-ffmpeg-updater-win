"""Logging Module."""

import logging

from core.const import LOG_MAP


def init_logging(log_level):
    """Init logging function.
    Used for new processes that don't have configured `root` logger.
    """
    log_format = '%(asctime)s %(module)-9s %(processName)-24s %(name)-21s %(funcName)-22s %(levelname)-8s %(message)s'
    logging.basicConfig(format=log_format, level=LOG_MAP[log_level])
    logging.getLogger('urllib3').setLevel(logging.WARNING)
