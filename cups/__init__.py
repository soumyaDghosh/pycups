from .connection import (
    Connection,
)
from .generic import (
    getEncryption,
    setEncryption,
    getPort,
    setPort,
    getServer,
    setServer,
    getUser,
    setUser,
    setDefaultDest,
)

from ._cups import lib, ffi

del connection  # noqa
del generic  # noqa

__all__ = [
    "Connection",
    "getEncryption",
    "setEncryption",
    "getPort",
    "setPort",
    "getServer",
    "setServer",
    "getUser",
    "setUser",
    "setDefaultDest",
    "lib",
    "ffi",
]
