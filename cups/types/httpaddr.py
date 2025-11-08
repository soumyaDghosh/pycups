import socket

from cups.types.base import _ffi, _lib, cupsBaseClass
from cups.utils import _bytes_to_value, _value_to_bytes


class HttpAddr(cupsBaseClass):
    """HTTP address structure."""

    __module__ = "cups.types"

    ffi_name = "http_addr_t"

    def close(self, fd: int):
        """Close a socket created by httpAddrConnect or httpAddrListen."""
        _lib.httpAddrClose(self.ffi_value, fd)

    @property
    def port(self) -> int:
        """Return the port number."""
        return _lib.httpAddrGetPort(self.ffi_value)

    @port.setter
    def port(self, value: int):
        """Set the port number."""
        _lib.httpAddrSetPort(self.ffi_value, value)

    @property
    def family(self) -> int:
        """Return the address family."""
        return _lib.httpAddrGetFamily(self.ffi_value)

    @family.setter
    def family(self, value: int):
        """Set the address family."""
        _lib.httpAddrSetFamily(self.ffi_value, value)

    @property
    def hostname(self) -> str:
        """Return the hostname."""
        c_str = _ffi.new("char[]", 256)
        _lib.httpAddrLookup(self.ffi_value, c_str, 256)
        return _bytes_to_value(c_str)

    @property
    def is_any(self) -> bool:
        """Return whether the address is a wildcard address."""
        return bool(_bytes_to_value(_lib.httpAddrIsAny(self.ffi_value)))

    @property
    def is_localhost(self) -> bool:
        """Return whether the address is a localhost address."""
        return bool(_bytes_to_value(_lib.httpAddrIsLocalhost(self.ffi_value)))

    def listen(self, port: int) -> int:
        """Create a listening socket bound to the specified address and port."""
        return _lib.httpAddrListen(self.ffi_value, port)

    def __eq__(self, value):
        return bool(
            _bytes_to_value(_lib.httpAddrEqual(self.ffi_value, value.ffi_value))
        )

    def __len__(self) -> int:
        """Return the size of the address structure."""
        return _lib.httpAddrGetLength(self.ffi_value)

    def __str__(self) -> str:
        """Return the string representation of the address."""
        c_str = _ffi.new("char[]", 1024)
        _lib.httpAddrGetString(self.ffi_value, c_str, 1024)
        return _bytes_to_value(c_str)


class HttpAddrList(cupsBaseClass):
    """HTTP address list structure."""

    __module__ = "cups.types"

    ffi_name = "http_addrlist_t"

    def connect(self, *, socket: int, msec: int) -> "HttpAddrList":
        """Connect to one of the addresses in the list."""
        addr_ptr = _lib.httpAddrListConnect(self.ffi_value, socket, msec, _ffi.NULL)
        if addr_ptr == _ffi.NULL:
            return None
        return HttpAddrList(ffi_value=addr_ptr)

    @staticmethod
    def getList(cls, hostname: str, family: socket.AddressFamily) -> "HttpAddrList":
        """Get a list of addresses for the specified hostname, family, and port."""
        c_hostname = _ffi.new("char[]", _value_to_bytes(hostname))
        addr_ptr = _lib.httpAddrGetList(c_hostname, family.value, _ffi.NULL)
        if addr_ptr == _ffi.NULL:
            return None
        return cls(ffi_value=addr_ptr)
