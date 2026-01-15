"""Utils Module."""

import asyncio
import functools
import logging
import re
from collections.abc import Awaitable
from typing import Any, TypeVar
from zipfile import ZipFile

from packaging.version import Version

from app.clients.codexffmpeg import ByteResponse
from app.exceptions import CommandError


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
    log: logging.Logger | None = None,
    raise_on_stderr: bool = False,
    timeout: float = 10,
) -> str:
    log = log or logging.getLogger(__name__)
    proc = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout)
    except TimeoutError as err:
        proc.kill()
        await proc.wait()
        log.error('Command "%s" timed out after %s seconds', cmd, timeout)  # noqa: TRY400
        raise CommandError(f'Command timed out: {cmd}') from err

    log.debug('Command "%s" exited with returncode %s', cmd, proc.returncode)

    stdout_decoded = stdout.decode(errors='replace')
    stderr_decoded = stderr.decode(errors='replace')

    if stderr_decoded:
        log.warning('[stderr] %s', stderr_decoded)
        if raise_on_stderr:
            raise CommandError(stderr_decoded)
    return stdout_decoded


T = TypeVar('T')


def create_task[T](  # noqa: PLR0913
    coroutine: Awaitable[T],
    *,
    logger: logging.Logger,
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
            logger=logger,
            exception_message=exception_message,
            exception_message_args=exception_message_args,
        )
    )
    return task


def _handle_task_result(
    task: asyncio.Task,
    *,
    logger: logging.Logger,
    exception_message: str,
    exception_message_args: tuple[Any, ...] = (),
) -> None:
    try:
        task.result()
    except asyncio.CancelledError:
        pass
    except Exception:
        logger.exception(exception_message, *exception_message_args)
