"""API Client Module."""

import abc
import logging

from aiohttp import ClientSession, TCPConnector


class AbstractApiClient(abc.ABC):
    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug('Initializing %s', self.__class__.__name__)
        self._session = ClientSession(connector=TCPConnector(verify_ssl=False),
                                      raise_for_status=True)

    async def close_session(self):
        self._log.debug('Closing session')
        await self._session.close()

    @abc.abstractmethod
    async def download_latest_version(self):
        pass
