"""API Client Module."""

import abc
import logging

from aiohttp import ClientSession, TCPConnector


class AbstractApiClient(abc.ABC):
    def __init__(self) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)
        self._session = ClientSession(
            connector=TCPConnector(verify_ssl=False), raise_for_status=True
        )

    async def _get_text(self, url: str) -> str:
        """Get text from request."""
        self._log.debug('GET %s', url)
        async with self._session.get(url) as response:
            return await response.text()

    async def close_session(self) -> None:
        """Close `ClientSession`."""
        self._log.debug('Close client session')
        await self._session.close()

    @abc.abstractmethod
    async def download_latest_version(self) -> None:
        pass
