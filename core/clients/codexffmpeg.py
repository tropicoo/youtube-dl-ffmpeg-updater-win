import abc
from dataclasses import dataclass
from enum import StrEnum
from io import BytesIO

from core.clients.abstract import AbstractApiClient
from core.constants import CHUNK_SIZE
from core.enums import CodexBuildType, CodexReleaseType
from core.third_party.stream_unzip import stream_unzip


class CodexApiPath(StrEnum):
    CHANGELOG_COUNTER = 'changelog-counter'

    LATEST_GIT_VER = 'git-version'
    LATEST_RELEASE_VER = 'release-version'
    LATEST_TOOLS_VER = 'tools-version'

    LAST_BUILD_UPDATE = 'last-build-update'
    NEXT_BUILD_UPDATE = 'next-build-update'


class CodexArchExtension(StrEnum):
    ZIP = 'zip'
    SEVEN_ZIP = '7z'


@dataclass
class ByteResponse:
    bytes_data: BytesIO
    headers: dict
    url: str


class AbstractCodexFFAPIClient(AbstractApiClient, abc.ABC):
    BUILDS_URL: str

    async def download_latest_version(
        self,
        release_type: CodexReleaseType = CodexReleaseType.RELEASE,
        build_type: CodexBuildType = CodexBuildType.ESSENTIALS,
    ):
        latest_version = await self.get_latest_version()

        async def zipped_chunks_generator():
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
    @abc.abstractmethod
    def _make_archive_filename(
        release_type: CodexReleaseType,
        build_type: CodexBuildType,
        build_version: str,
        extension: CodexArchExtension = CodexArchExtension.ZIP,
    ) -> str:
        """Make zip archive filename to append to download url."""

    @abc.abstractmethod
    async def _make_download_url(self, filename: str, build_version: str) -> str:
        pass

    @abc.abstractmethod
    async def get_latest_version(self) -> str:
        pass


class CodexFFAPIClient(AbstractCodexFFAPIClient):
    BUILDS_URL = 'https://www.gyan.dev/ffmpeg/builds/'
    _TYPE_MAP = {
        CodexReleaseType.RELEASE: BUILDS_URL + CodexApiPath.LATEST_RELEASE_VER,
        CodexReleaseType.GIT: BUILDS_URL + CodexApiPath.LATEST_GIT_VER,
    }

    async def get_changelog_counter(self) -> str:
        return await self._get_text(self.BUILDS_URL + CodexApiPath.CHANGELOG_COUNTER)

    async def get_latest_version(
        self, release_type: CodexReleaseType = CodexReleaseType.RELEASE
    ) -> str:
        return await self._get_text(self._TYPE_MAP[release_type])

    async def get_last_build_date(self) -> str:
        return await self._get_text(self.BUILDS_URL + CodexApiPath.LAST_BUILD_UPDATE)

    async def get_next_build_date(self) -> str:
        return await self._get_text(self.BUILDS_URL + CodexApiPath.NEXT_BUILD_UPDATE)

    def _make_download_url(self, filename: str, build_version: str) -> str:
        return self.BUILDS_URL + filename

    @staticmethod
    def _make_archive_filename(
        release_type: CodexReleaseType,
        build_type: CodexBuildType,
        build_version: str,
        extension: CodexArchExtension = CodexArchExtension.ZIP,
    ) -> str:
        """Make zip archive filename to append to download url."""
        return f'ffmpeg-{release_type}-{build_type}.{extension}'


class CodexFFGithubApiClient(AbstractCodexFFAPIClient):
    HOST = 'https://github.com/GyanD/codexffmpeg'
    BUILDS_URL = f'{HOST}/releases/download/{{tag}}/{{filename}}'
    LATEST_TAG_URL = f'{HOST}/releases/latest'

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
        release_type: CodexReleaseType,
        build_type: CodexBuildType,
        build_version: str,
        extension: CodexArchExtension = CodexArchExtension.ZIP,
    ) -> str:
        """Make zip archive filename to append to download url."""
        return f'ffmpeg-{build_version}-{build_type}_build.{extension}'
