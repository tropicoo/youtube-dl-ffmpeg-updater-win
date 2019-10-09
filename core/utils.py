"""Utils Module."""

from multiprocessing.managers import BaseManager


def init_shared_manager(items):
    for cls in items:
        BaseManager.register(cls.__name__, cls)
    manager = BaseManager()
    manager.start()
    return manager
