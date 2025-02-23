from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator
from dataclasses import dataclass
from io import BytesIO
from typing import ClassVar, Literal

from app.clients.abstract import AbstractApiClient
from app.constants import CHUNK_SIZE
from app.enums import (
    CodexApiPathType,
    CodexArchExtensionType,
    CodexBuildType,
    CodexReleaseType,
)
from app.third_party.stream_unzip import stream_unzip


@dataclass
class ByteResponse:
    bytes_data: BytesIO
    headers: dict
    url: str


class AbstractCodexFFAPIClient(AbstractApiClient, ABC):
    BUILDS_URL: str | None = None

    async def download_latest_version(
        self,
        release_type: Literal[CodexReleaseType.RELEASE] = CodexReleaseType.RELEASE,
        build_type: Literal[CodexBuildType.ESSENTIALS] = CodexBuildType.ESSENTIALS,
    ) -> AsyncGenerator[tuple[bytes, int, AsyncGenerator[bytes, None]], None]:
        latest_version = await self.get_latest_version()
        self._log.info('Latest version: "%s"', latest_version)

        async def zipped_chunks_generator() -> AsyncGenerator[bytes, None]:
            """Async zip archive chunks generator."""
            zip_filename = self._make_archive_filename(
                release_type=release_type,
                build_type=build_type,
                build_version=latest_version,
            )
            url = await self._make_download_url(
                filename=zip_filename, build_version=latest_version
            )
            self._log.debug('GET %s', url)
            self._log.debug('Start download %s', zip_filename)
            async with self._session.get(url) as response:
                async for chunk in response.content.iter_chunked(CHUNK_SIZE):
                    yield chunk
                self._log.debug('End download %s', zip_filename)

        async for filename, file_size, unzipped_chunks in stream_unzip(
            zipped_chunks_generator()
        ):
            yield filename, file_size, unzipped_chunks

    @staticmethod
    @abstractmethod
    def _make_archive_filename(
        release_type: CodexReleaseType,
        build_type: CodexBuildType,
        build_version: str,
        extension: Literal[CodexArchExtensionType.ZIP] = CodexArchExtensionType.ZIP,
    ) -> str:
        """Make zip archive filename to append to download url."""

    @abstractmethod
    async def _make_download_url(self, filename: str, build_version: str) -> str:
        pass

    @abstractmethod
    async def get_latest_version(self) -> str:
        pass


class CodexFFAPIClient(AbstractCodexFFAPIClient):
    BUILDS_URL: str = 'https://www.gyan.dev/ffmpeg/builds/'
    _TYPE_MAP: ClassVar[dict[CodexReleaseType, str]] = {
        CodexReleaseType.RELEASE: BUILDS_URL + CodexApiPathType.LATEST_RELEASE_VER,
        CodexReleaseType.GIT: BUILDS_URL + CodexApiPathType.LATEST_GIT_VER,
    }

    async def get_changelog_counter(self) -> str:
        return await self._get_text(
            self.BUILDS_URL + CodexApiPathType.CHANGELOG_COUNTER
        )

    async def get_latest_version(
        self, release_type: CodexReleaseType = CodexReleaseType.RELEASE
    ) -> str:
        return await self._get_text(self._TYPE_MAP[release_type])

    async def get_last_build_date(self) -> str:
        return await self._get_text(
            self.BUILDS_URL + CodexApiPathType.LAST_BUILD_UPDATE
        )

    async def get_next_build_date(self) -> str:
        return await self._get_text(
            self.BUILDS_URL + CodexApiPathType.NEXT_BUILD_UPDATE
        )

    def _make_download_url(self, filename: str, build_version: str) -> str:  # noqa: ARG002
        return self.BUILDS_URL + filename

    @staticmethod
    def _make_archive_filename(
        release_type: CodexReleaseType,
        build_type: CodexBuildType,
        build_version: str,  # noqa: ARG004
        extension: Literal[CodexArchExtensionType.ZIP] = CodexArchExtensionType.ZIP,
    ) -> str:
        """Make zip archive filename to append to download url."""
        return f'ffmpeg-{release_type}-{build_type}.{extension}'


class CodexFFGithubApiClient(AbstractCodexFFAPIClient):
    HOST: str = 'https://github.com/GyanD/codexffmpeg'
    BUILDS_URL: str = f'{HOST}/releases/download/{{tag}}/{{filename}}'
    LATEST_TAG_URL: str = f'{HOST}/releases/latest'

    async def _make_download_url(self, filename: str, build_version: str) -> str:
        return self.BUILDS_URL.format(tag=build_version, filename=filename)

    async def get_latest_version(self) -> str:
        return await self._get_latest_tag()

    async def _get_latest_tag(self) -> str:
        self._log.debug('GET %s', self.LATEST_TAG_URL)
        async with self._session.get(self.LATEST_TAG_URL) as response:
            return response.url.name

    @staticmethod
    def _make_archive_filename(
        release_type: CodexReleaseType,  # noqa: ARG004
        build_type: CodexBuildType,
        build_version: str,
        extension: Literal[CodexArchExtensionType.ZIP] = CodexArchExtensionType.ZIP,
    ) -> str:
        """Make zip archive filename to append to download url."""
        return f'ffmpeg-{build_version}-{build_type}_build.{extension}'
