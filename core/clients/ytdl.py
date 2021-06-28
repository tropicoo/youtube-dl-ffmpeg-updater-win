"""API Client Module."""

from core.clients.abstract import AbstractApiClient
from core.constants import CHUNK_SIZE, URL_YTDL


class YouTubeDLAPIClient(AbstractApiClient):

    async def download_latest_version(self):
        """Download the latest version of youtube-dl executable."""
        async with self._session.get(URL_YTDL) as response:
            async for data in response.content.iter_chunked(CHUNK_SIZE):
                yield data
