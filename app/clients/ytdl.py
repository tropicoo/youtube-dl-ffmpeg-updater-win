"""API Client Module."""

from collections.abc import AsyncIterator

from aiohttp import ClientResponseError

from app.clients.abstract import AbstractApiClient
from app.constants import CHUNK_SIZE, URL_YTDL


class YTDLApiClient(AbstractApiClient):
    async def download_latest_version(self) -> AsyncIterator[bytes]:
        """Download the latest version of youtube-dl executable."""
        try:
            async with self._session.get(URL_YTDL) as response:
                async for chunk in response.content.iter_chunked(CHUNK_SIZE):
                    yield chunk
        except ClientResponseError as err:
            self._log.error('Failed to download %s: "%s"', URL_YTDL, err)
