from ._cups import ffi, lib  # noqa: D104
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

del connection  # noqa: F821
del generic  # noqa: F821

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
