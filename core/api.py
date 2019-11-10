"""API Client Module."""

import logging
import requests

from core.const import HTTP, URL_YTDL
from core.log import init_logging


class BaseHTTPClient:
    def __init__(self, log_level):
        init_logging(log_level)
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)

    def _request(self, url, method=HTTP.GET, stream=False):
        """General Request Method."""
        self._log.debug('%s %s', method, url)
        return requests.request(method=method, url=url, stream=stream)


class YouTubeDLAPIClient(BaseHTTPClient):
    def __init__(self, log_level):
        super().__init__(log_level)

    def download_latest_version(self):
        return self._request(url=URL_YTDL, stream=True)
