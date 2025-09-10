from ._cups import ffi, lib  # type: ignore[import-not-found]  # noqa: D104
from .connection import (
    Connection,
)
from .generic import (
    areCredentialsValidForName,
    copyCredentialsKey,
    copyDest,
    getDestWithURI,
    getEncryption,
    getError,
    getPort,
    getServer,
    getUser,
    getUserAgent,
    setDefaultDest,
    setEncryption,
    setPort,
    setServer,
    setUser,
    setUserAgent,
)

del connection  # type: ignore[name-defined]  # noqa: F821
del generic  # type: ignore[name-defined]  # noqa: F821

__all__ = [
    "Connection",
    "areCredentialsValidForName",
    "copyCredentialsKey",
    "copyDest",
    "getDestWithURI",
    "getEncryption",
    "setEncryption",
    "getError",
    "getPort",
    "setPort",
    "getServer",
    "setServer",
    "getUser",
    "setUser",
    "getUserAgent",
    "setUserAgent",
    "setDefaultDest",
    "lib",
    "ffi",
]
