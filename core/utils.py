"""Utils Module."""

import asyncio
import functools
import logging
import re
from distutils.version import LooseVersion, StrictVersion
from typing import Any, Awaitable, TypeVar
from zipfile import ZipFile

from core.clients.codexffmpeg import ByteResponse
from core.exceptions import CommandError


def response_to_zip(data: ByteResponse, filename: str = None) -> ZipFile:
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


def get_largest_value(items: list, strict=True) -> str:
    conv_cls = StrictVersion if strict else LooseVersion
    return str(max([conv_cls(x) for x in items]))


async def get_stdout(
    cmd: str, log: logging.Logger = None, raise_on_stderr: bool = False
) -> str:
    if not log:
        log = logging.getLogger()
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    log.debug('Command "%s" exited with returncode %s', cmd, proc.returncode)
    if stderr:
        log.warning('[stderr] %s', stderr.decode())
        if raise_on_stderr:
            raise CommandError(stderr)
    return stdout.decode()


T = TypeVar('T')


def create_task(
    coroutine: Awaitable[T],
    *,
    logger: logging.Logger,
    task_name: str = None,
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
