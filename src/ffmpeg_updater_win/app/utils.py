"""Utils Module."""

import asyncio
import functools
import re
from collections.abc import Coroutine
from io import StringIO
from typing import TYPE_CHECKING, Any, Final
from zipfile import ZipFile

from loguru import logger
from packaging.version import Version
from rich.console import Console

from ffmpeg_updater_win.app.clients.codex_ffmpeg.models import ByteResponse
from ffmpeg_updater_win.app.exceptions import CommandError

if TYPE_CHECKING:
    from loguru import Logger  # noqa: TC004

rich_console: Final[Console] = Console()


def response_to_zip(data: ByteResponse, filename: str | None = None) -> ZipFile:
    """Create zip-like file object from `requests` response and set its real filename."""
    zip_obj = ZipFile(data.bytes_data)
    if not filename:
        filename = get_filename_from_header(data.headers) or get_filename_from_url(
            data.url
        )
    zip_obj.filename = filename
    return zip_obj


def get_filename_from_header(headers: dict) -> str:
    match = re.search(r'filename=(.+)', headers.get('Content-Disposition', ''))
    return match.group(1) if match else ''


def get_filename_from_url(url: str) -> str:
    return url.rsplit('/', 1)[-1]


def get_largest_value(items: list[str]) -> str:
    """Return the string representation of the highest version.

    Assumes items are PEP 440 compatible version strings.
    Raises InvalidVersion if any value cannot be parsed.
    """
    return str(max(map(Version, items)))


async def get_stdout(
    cmd: list[str] | tuple[str, ...],
    log: Logger | None = None,
    raise_on_stderr: bool = False,
    timeout: float = 10,
) -> str:
    log = log or logger
    proc = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout)
    except TimeoutError as err:
        proc.kill()
        await proc.wait()
        log.error('Command "{}" timed out after {} seconds', cmd, timeout)  # noqa: TRY400
        raise CommandError(f'Command timed out: {cmd}') from err

    log.debug('Command "{}" exited with returncode {}', cmd, proc.returncode)

    stdout_decoded = stdout.decode(errors='replace')
    stderr_decoded = stderr.decode(errors='replace')

    if stderr_decoded:
        log.warning('[stderr] {}', stderr_decoded)
        if raise_on_stderr:
            raise CommandError(stderr_decoded)
    return stdout_decoded


def create_task[T](  # noqa: PLR0913
    coroutine: Coroutine[Any, Any, T],
    *,
    log: Logger,
    task_name: str | None = None,
    exception_message: str = 'Task raised an exception',
    exception_message_args: tuple[Any, ...] = (),
    loop: asyncio.AbstractEventLoop | None = None,
) -> asyncio.Task[T]:
    if loop is None:
        loop = asyncio.get_running_loop()
    task = loop.create_task(coroutine, name=task_name)
    task.add_done_callback(
        functools.partial(
            _handle_task_result,
            log=log,
            exception_message=exception_message,
            exception_message_args=exception_message_args,
        )
    )
    return task


def _handle_task_result(
    task: asyncio.Task,
    *,
    log: Logger,
    exception_message: str,
    exception_message_args: tuple[Any, ...] = (),
) -> None:
    try:
        task.result()
    except asyncio.CancelledError:
        pass
    except Exception:
        log.exception(exception_message, *exception_message_args)


def render_to_ansi(renderable: Any, *, width: int | None = None) -> str:
    buf = StringIO()
    console = Console(file=buf, width=width)
    console.print(renderable)
    return buf.getvalue()
