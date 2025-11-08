from ._cups import ffi, lib
from .cupslang import (
    langAddStrings,
    langDefault,
    langFind,
    langGetEncoding,
    langGetString,
)
from .generic import (
    areCredentialsValidForName,
    copyCredentialsKey,
    # copyDest,
    # getDestWithURI,
    getEncryption,
    getError,
    getPort,
    getServer,
    getUser,
    getUserAgent,
    setEncryption,
    setPort,
    setServer,
    setUser,
    setUserAgent,
    # setDefaultDest,
)

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
