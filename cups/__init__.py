from ._cups import ffi, lib
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

del connection  # noqa
del generic  # noqa

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
