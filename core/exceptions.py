"""Exceptions Module."""


class BaseUpdaterError(Exception):
    pass


class UpdaterError(BaseUpdaterError):
    """Updater Base Exception Class."""

    pass


class NoFileToExtractError(UpdaterError):
    pass


class CommandError(UpdaterError):
    pass
