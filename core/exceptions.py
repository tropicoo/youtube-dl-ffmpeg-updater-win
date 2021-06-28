"""Exceptions Module."""


class UpdaterError(Exception):
    """Updater Base Exception Class."""
    pass


class NoFileToExtractError(UpdaterError):
    pass
