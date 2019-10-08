"""API Client Module."""

import logging
import requests
import time

from core.const import HTTP, URL_YTDL, FFBINARIES_API


class BaseHTTPClient:
    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)

    def _request(self, url, method=HTTP.GET, stream=False):
        """General Request Method."""
        self._log.debug('%s %s', method, url)
        return requests.request(method=method, url=url, stream=stream)


class YouTubeDLAPIClient(BaseHTTPClient):
    def download_latest_version(self):
        return self._request(url=URL_YTDL, stream=True)


class FFBinariesAPIClient(BaseHTTPClient):
    CACHE_EXPIRE_TIME = 300
    CACHE_METADATA = None
    CACHE_FETCH_TIME = None

    def get_latest_metadata(self):
        if self.CACHE_METADATA is None or \
                time.time() - self.CACHE_FETCH_TIME > self.CACHE_EXPIRE_TIME:
            self.CACHE_METADATA = self._request(url=FFBINARIES_API).json()
            self.CACHE_FETCH_TIME = time.time()
            return self.CACHE_METADATA
        return self.CACHE_METADATA

    def get_latest_version(self):
        return self.get_latest_metadata()['version']

    def download_latest_version(self, platform, component):
        metadata = self.get_latest_metadata()['bin'][platform]
        return self._request(url=metadata[component]).content
