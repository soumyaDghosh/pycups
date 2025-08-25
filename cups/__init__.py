from .connection import (
    Connection,
)
from .generic import (
    areCredentialsValidForName,
    copyCredentialsKey,
    copyDest,
    getDestWithURI,
    getEncryption,
    setEncryption,
    getError,
    getPort,
    setPort,
    getServer,
    setServer,
    getUser,
    setUser,
    getUserAgent,
    setUserAgent,
    setDefaultDest,
)

from ._cups import lib, ffi

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
