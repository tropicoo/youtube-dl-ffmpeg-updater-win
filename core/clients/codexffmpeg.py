from dataclasses import dataclass
from io import BytesIO

from core.clients.abstract import AbstractApiClient
from core.constants import CodexBuildType, CodexReleaseType


class CodexApiPath:
    CHANGELOG_COUNTER = 'changelog-counter'

    LATEST_GIT_VER = 'git-version'
    LATEST_RELEASE_VER = 'release-version'
    LATEST_TOOLS_VER = 'tools-version'

    LAST_BUILD_UPDATE = 'last-build-update'
    NEXT_BUILD_UPDATE = 'next-build-update'


class CodexArchExtension:
    ZIP = 'zip'
    SEVEN_ZIP = '7z'


@dataclass
class ByteResponse:
    bytes_data: BytesIO
    headers: dict
    url: str


class CodexFFAPIClient(AbstractApiClient):
    BUILDS_URL = 'https://www.gyan.dev/ffmpeg/builds/'
    _TYPE_MAP = {
        CodexReleaseType.RELEASE: BUILDS_URL + CodexApiPath.LATEST_RELEASE_VER,
        CodexReleaseType.GIT: BUILDS_URL + CodexApiPath.LATEST_GIT_VER,
    }

    async def _get_text(self, url: str) -> str:
        async with self._session.get(url) as response:
            return await response.text()

    async def get_changelog_counter(self) -> str:
        return await self._get_text(self.BUILDS_URL + CodexApiPath.CHANGELOG_COUNTER)

    async def get_latest_version(self, release_type=CodexReleaseType.RELEASE) -> str:
        return await self._get_text(self._TYPE_MAP[release_type])

    async def get_last_build_date(self) -> str:
        return await self._get_text(self.BUILDS_URL + CodexApiPath.LAST_BUILD_UPDATE)

    async def get_next_build_date(self) -> str:
        return await self._get_text(self.BUILDS_URL + CodexApiPath.NEXT_BUILD_UPDATE)

    async def download_latest_version(self,
                                      release_type: str = CodexReleaseType.RELEASE,
                                      build_type: str = CodexBuildType.ESSENTIALS) -> ByteResponse:
        url = self.BUILDS_URL + self._make_archive_path(release_type, build_type)
        async with self._session.get(url) as response:
            return ByteResponse(bytes_data=BytesIO(await response.read()),
                                headers=dict(response.headers),
                                url=str(url))

    @staticmethod
    def _make_archive_path(release_type: str, build_type: str,
                           extension: str = CodexArchExtension.ZIP) -> str:
        return f'ffmpeg-{release_type}-{build_type}.{extension}'
