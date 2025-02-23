"""Exceptions Module."""


class BaseUpdaterError(Exception):
    pass


class UpdaterError(BaseUpdaterError):
    """Updater Base Exception Class."""


class NoFileToExtractError(UpdaterError):
    pass


class CommandError(UpdaterError):
    pass
