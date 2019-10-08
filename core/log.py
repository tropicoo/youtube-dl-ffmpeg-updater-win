"""Logging Module."""

import logging


def init_logging():
    log_format = '%(asctime)s %(levelname)-8s %(name)-30s %(processName)-22s [%(funcName)-27s,%(lineno)d] %(message)s'
    logging.basicConfig(format=log_format, level=logging.DEBUG)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
