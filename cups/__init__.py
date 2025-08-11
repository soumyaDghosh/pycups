from cups.connection import (
    Connection,
)

from cups.generic import (
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

from cups._cups import lib, ffi

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
