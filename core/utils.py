"""Utils Module."""

import re
from io import BytesIO
from multiprocessing.managers import BaseManager
from zipfile import ZipFile


def init_shared_manager(items):
    """Initialize and start shared manager."""
    for cls in items:
        BaseManager.register(cls.__name__, cls)
    manager = BaseManager()
    manager.start()
    return manager


def response_to_zip(response):
    """Create zip-like file object from `requests` response and set its real
    filename.
    """
    filename = re.search(r'filename=(.+)',
                         response.headers['Content-Disposition']).group(1)
    _zip = ZipFile(BytesIO(response.content))
    _zip.filename = filename
    return _zip
