"""API Client Module."""

from abc import ABC, abstractmethod
from typing import Any

from aiohttp import ClientSession, TCPConnector
from loguru import logger


class BaseApiClient(ABC):
    def __init__(self) -> None:
        self._log = logger
        self._log.debug('Initializing "{}"', self.__class__.__name__)
        self._session = ClientSession(
            connector=TCPConnector(verify_ssl=False), raise_for_status=True
        )

    async def _get_text(self, url: str) -> str:
        """Get text from request."""
        self._log.debug('GET {}', url)
        async with self._session.get(url) as response:
            return await response.text()

    async def close_session(self) -> None:
        """Close `ClientSession`."""
        self._log.debug('Close client session')
        await self._session.close()

    @abstractmethod
    async def download_latest_version(self) -> Any:
        pass
