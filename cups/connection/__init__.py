from cups import _cups
from cups.generic import (
    getEncryption,
    getPort,
    getServer,
    getUser,
    setEncryption,
    setPort,
    setServer,
    setUser,
)
from cups.enums.http import HttpEncryption, HttpStatus
from typing import Any, Optional

from .dests import DestsMixin
from .jobs import JobMixin
from .base import _Base
from cups.utils import _bytes_to_value

import socket

_ffi = _cups.ffi
_lib = _cups.lib


class Connection(DestsMixin, JobMixin, _Base):
    """Connection to the CUPS server."""

    http: Any
    __module__: str = "cups"

    @property
    def host(self) -> str:
        """Return the host of the CUPS server."""
        return getServer()

    @host.setter
    def host(self, host: str):
        setServer(host)

    @property
    def port(self) -> int:
        """Return the port of the CUPS server."""
        return getPort()

    @port.setter
    def port(self, port: int):
        setPort(port)

    @property
    def encryption(self) -> HttpEncryption:
        """Return the encryption type used for the connection."""
        return getEncryption()

    @encryption.setter
    def encryption(self, encryption: HttpEncryption):
        setEncryption(encryption)

    @property
    def user(self) -> str:
        return getUser()

    @user.setter
    def user(self, user: str):
        setUser(user)

    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        encryption: Optional[HttpEncryption] = None,
        family: socket.AddressFamily = socket.AF_UNSPEC,
        msec: int = 0,
    ):
        if host:
            self.host = host

        if port:
            self.port = port

        if encryption:
            self.encryption = encryption

        c_host = _ffi.new("char []", self.host.encode())
        c_port = _ffi.cast("int", self.port)
        c_encryption = _ffi.cast("http_encryption_t", self.encryption)
        self.http = _lib.httpConnect(
            c_host, c_port, _ffi.NULL, family, c_encryption, True, msec, _ffi.NULL
        )

    def connectAgain(self, msec: int) -> bool:
        return bool(_lib.httpConnectAgain(self.http, msec, _ffi.NULL))

    def doAuthentication(self, method: str, resource: str) -> bool:
        return bool(_lib.cupsDoAuthentication(self.http, method.encode(), resource.encode()))

    def getPassword(self, prompt: str, method: str, resource: str) -> str:
        return _bytes_to_value(
            _lib.cupsGetPassword(
                prompt.encode(), self.http, method.encode(), resource.encode()
            )
        )

    def getFile(self, resource: str, filname: str) -> HttpStatus:
        return HttpStatus(
            _lib.cupsGetFile(self.http, resource.encode(), filname.encode())
        )
