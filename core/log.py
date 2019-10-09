"""Logging Module."""

import logging


def init_logging():
    log_format = '%(asctime)s %(module)-9s %(processName)-22s %(name)-25s %(funcName)-10s %(levelname)-8s %(message)s'
    logging.basicConfig(format=log_format, level=logging.DEBUG)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
