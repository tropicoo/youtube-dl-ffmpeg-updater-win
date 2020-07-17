"""Unittests for Updater API."""

import time
import unittest
from unittest.mock import PropertyMock, patch

import requests
from ffbinaries import FFBinariesAPIClient

import core.const as const
from core.api import YouTubeDLAPIClient

LOG_LEVEL = 3  # DEBUG

LATEST_VERSION = '4.2'

WIN_32 = 'windows-32'
WIN_64 = 'windows-64'
PLATFORM_MAP = {WIN_32: 'win-32',
                WIN_64: 'win-64'}

FILENAME_PATTERN_FF = '{component}-{version}-{platform}.zip'
HEADER_CONTENT_LENGTH = 'Content-Length'
HEADER_CONTENT_DISPOSITION = 'Content-Disposition'
HEADER_CONTENT_DISPOSITION_VALUE = 'attachment; filename={filename}'

STATUS_CODE_OK = 200

LATEST_JSON = {'version': '4.2',
               'permalink': 'http://ffbinaries.com/api/v1/version/4.2',
               'bin': {'windows-32': {
                   'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-win-32.zip',
                   'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-win-32.zip',
                   'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-win-32.zip'},
                   'windows-64': {
                       'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-win-64.zip',
                       'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-win-64.zip',
                       'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-win-64.zip'},
                   'linux-32': {
                       'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-32.zip',
                       'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-32.zip'},
                   'linux-64': {
                       'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-64.zip',
                       'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-64.zip'},
                   'linux-armhf': {
                       'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-armhf-32.zip',
                       'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-armhf-32.zip'},
                   'linux-armel': {
                       'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-armel-32.zip',
                       'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-armel-32.zip'},
                   'linux-arm64': {
                       'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-arm-64.zip',
                       'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-arm-64.zip'},
                   'osx-64': {
                       'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-osx-64.zip',
                       'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-osx-64.zip',
                       'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-osx-64.zip'}}}

BINARY_CONTENT_DUMMY = b'<binary_content>'


def make_response(content_disposition_value):
    res = requests.models.Response()
    res.status_code = STATUS_CODE_OK
    type(res).content = PropertyMock(return_value=BINARY_CONTENT_DUMMY)
    res.headers = {HEADER_CONTENT_DISPOSITION: content_disposition_value,
                   HEADER_CONTENT_LENGTH: str(len(BINARY_CONTENT_DUMMY))}
    return res


class TestYouTubeDLAPIClient(unittest.TestCase):
    def setUp(self):
        self._api = YouTubeDLAPIClient(LOG_LEVEL)

    @patch.object(requests, 'request')
    def test_download_latest_version(self, mock_request):
        header_value = HEADER_CONTENT_DISPOSITION_VALUE.format(
            filename=const.EXE_YTDL)
        mock_request.return_value = make_response(header_value)

        obj = self._api.download_latest_version()
        self.assertIsInstance(obj, requests.models.Response)
        self.assertEqual(obj.status_code, STATUS_CODE_OK)

        self.assertEqual(HEADER_CONTENT_DISPOSITION_VALUE.format(
            filename=const.EXE_YTDL),
            obj.headers[HEADER_CONTENT_DISPOSITION])
        requests.request.assert_called_once_with(method=const.Http.GET,
                                                 url=const.URL_YTDL,
                                                 stream=True)


class TestFFBinariesAPIClient(unittest.TestCase):
    def setUp(self):
        self._api = FFBinariesAPIClient(LOG_LEVEL)
        self._platforms = tuple(map(lambda v: v['endpoint'],
                                    const.PLATFORMS.values()))
        self._components = tuple(map(lambda x: x.rsplit('.', 1)[0],
                                     const.REQUIRED_FFBINARIES))

    def _verify_data(self, obj, platform, component):
        self.assertIsInstance(obj, requests.models.Response)
        self.assertEqual(obj.status_code, STATUS_CODE_OK)

        self.assertEqual(len(obj.content),
                         int(obj.headers[HEADER_CONTENT_LENGTH]))

        self.assertEqual(obj.headers[HEADER_CONTENT_DISPOSITION],
                         HEADER_CONTENT_DISPOSITION_VALUE.format(
                             filename=FILENAME_PATTERN_FF.format(
                                 component=component,
                                 version=LATEST_VERSION,
                                 platform=platform)))

    @patch('core.api.FFBinariesAPIClient.get_latest_metadata',
           return_value=LATEST_JSON)
    @patch.object(requests, 'request')
    def test_download_latest_version(self, mock_request,
                                     get_latest_metadata_mock):
        for platform in self._platforms:
            for comp in self._components:
                filename_platform = PLATFORM_MAP[platform]
                header_value = HEADER_CONTENT_DISPOSITION_VALUE.format(
                    filename=FILENAME_PATTERN_FF.format(component=comp,
                                                        platform=filename_platform,
                                                        version=LATEST_VERSION))
                mock_request.return_value = make_response(header_value)
                obj = self._api.download_latest_version(platform=platform,
                                                        component=comp)
                self._verify_data(obj, filename_platform, comp)
                self._api.get_latest_metadata.assert_called_once()
                requests.request.assert_called_once_with(method=const.Http.GET,
                                                         url=
                                                         LATEST_JSON['bin'][
                                                             platform][comp],
                                                         stream=False)
                self._api.get_latest_metadata.reset_mock()
                requests.request.reset_mock()

    @patch('core.api.FFBinariesAPIClient.get_latest_metadata',
           return_value=LATEST_JSON)
    def test_get_latest_version(self, get_latest_metadata_mock):
        version = self._api.get_latest_version()
        self.assertEqual(version, LATEST_VERSION)
        self._api.get_latest_metadata.assert_called_once()

    @patch('core.api.FFBinariesAPIClient._request')
    def test_get_latest_metadata_non_cached(self, request_mock):
        request_mock.return_value.json = lambda: LATEST_JSON
        self.assertEqual(self._api.get_latest_metadata(), LATEST_JSON)
        self.assertEqual(self._api._cache_metadata, LATEST_JSON)
        self.assertIsInstance(self._api._cache_fetch_time, int)
        self._api._request.assert_called_once_with(url=const.FFBINARIES_API)

    @patch('core.api.FFBinariesAPIClient._request', return_value={})
    def test_get_latest_metadata_cached(self, mock_request):
        now = int(time.time())
        with patch.object(self._api, '_cache_metadata', LATEST_JSON), \
             patch.object(self._api, '_cache_fetch_time', now):
            self.assertEqual(self._api._cache_metadata, LATEST_JSON)
            self.assertEqual(self._api._cache_fetch_time, now)
            self.assertEqual(self._api.get_latest_metadata(), LATEST_JSON)
            self._api._request.assert_not_called()


if __name__ == '__main__':
    unittest.main()
