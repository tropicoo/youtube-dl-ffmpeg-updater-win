"""API Client Module."""

import logging
import requests
import time
from multiprocessing import Lock

from core.const import HTTP, URL_YTDL, FFBINARIES_API
from core.log import init_logging


class BaseHTTPClient:
    def __init__(self, log_level):
        init_logging(log_level)
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)

    def _request(self, url, method=HTTP.GET, stream=False):
        """General Request Method."""
        self._log.debug('%s %s ', method, url)
        return requests.request(method=method, url=url, stream=stream)


class YouTubeDLAPIClient(BaseHTTPClient):
    def __init__(self, log_level):
        super().__init__(log_level)

    def download_latest_version(self):
        return self._request(url=URL_YTDL, stream=True)


class FFBinariesAPIClient(BaseHTTPClient):
    def __init__(self, log_level):
        super().__init__(log_level)
        self._proc_lock = Lock()
        self._cache_expire_time = 300
        self._cache_metadata = None
        self._cache_fetch_time = None

    def get_latest_metadata(self):
        if self._cache_metadata is None or \
                time.time() - self._cache_fetch_time > self._cache_expire_time:
            self._cache_metadata = self._request(url=FFBINARIES_API).json()
            self._cache_fetch_time = time.time()
        return self._cache_metadata

    def get_latest_version(self):
        return self.get_latest_metadata()['version']

    def download_latest_version(self, platform, component):
        # Make only one request and use cached json metadata further.
        with self._proc_lock:
            metadata = self.get_latest_metadata()['bin'][platform]
        return self._request(url=metadata[component])
