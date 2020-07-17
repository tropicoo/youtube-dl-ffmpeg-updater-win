"""API Client Module."""

import logging

import requests

from core.const import (FFMPEG_FILE_ZERANOE_PATTERN, FFReleaseChannel,
                        FfmpegLinkingType, Http, URL_YTDL,
                        URL_ZERANOE_BUILDS_JSON, URL_ZERANOE_DOWNLOAD,
                        WinPlatform)
from core.log import init_logging
from core.utils import get_largest_value


class BaseHTTPClient:
    def __init__(self, log_level):
        init_logging(log_level)
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %r', self)

    def _request(self, url, method=Http.GET, stream=False):
        """General Request Method."""
        self._log.debug('%s %s', method, url)
        return requests.request(method=method, url=url, stream=stream)


class YouTubeDLAPIClient(BaseHTTPClient):

    def download_latest_version(self):
        """Download the latest version of youtube-dl."""
        return self._request(url=URL_YTDL, stream=True)


class FFBinariesZeranoeClient(BaseHTTPClient):

    def download_latest_version(self, platform=WinPlatform.WIN32,
                                release_channel=FFReleaseChannel.RELEASE,
                                linking_type=FfmpegLinkingType.STATIC):
        url = self._get_download_url(platform, release_channel, linking_type)
        return self._request(url=url, stream=True)

    def get_latest_version(self, release_channel=FFReleaseChannel.RELEASE):
        builds = self._get_builds_json()
        return self._get_latest_version(builds, release_channel)

    def _get_download_url(self, platform, release_channel, linking_type):
        latest_release = self.get_latest_version(release_channel)
        return self._build_download_url(latest_release, platform, linking_type)

    @staticmethod
    def _get_latest_version(builds, release_channel):
        strict = False
        if release_channel == FFReleaseChannel.RELEASE:
            strict = True
        return get_largest_value(builds['release'], strict=strict)

    @staticmethod
    def _build_download_url(build_version, platform, linking_type):
        filename = FFMPEG_FILE_ZERANOE_PATTERN.format(
            build_version=build_version, platform=platform,
            linking=linking_type)
        return URL_ZERANOE_DOWNLOAD.format(platform=platform,
                                           linking=linking_type,
                                           filename=filename)

    def _get_builds_json(self):
        return self._request(url=URL_ZERANOE_BUILDS_JSON).json()
