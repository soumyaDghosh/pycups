import socket
from datetime import datetime
from pathlib import Path
from typing import Optional

from cups.enums.http import (
    HttpEncryption,
    HttpField,
    HttpState,
    HttpStatus,
    HttpUriCoding,
    HttpUriStatus,
)
from cups.generic import getEncryption, getPort, getServer
from cups.types.base import _ffi, _lib, cupsBaseClass
from cups.types.httpaddr import HttpAddr
from cups.utils import _bytes_to_value, _value_to_bytes


class Http(cupsBaseClass):
    """HTTP connection to the CUPS server."""

    __module__ = "cups.types"

    ffi_name = "http_t"
    # host: str = getServer()
    # port: int = getPort()
    # family: socket.AddressFamily = socket.AF_UNSPEC
    # msec: int = 3000

    @classmethod
    def acceptConnection(cls, path: Path, *, blocking: bool) -> "Http":
        """Accept a new HTTP client connection."""
        if not path.exists():
            raise FileNotFoundError(f"Socket {path=} does not exist.")
        if not path.is_socket():
            raise OSError(f"{path=} is not a socket.")

        try:
            file = path.open()
        except Exception as e:
            raise e

        http_ptr = _lib.httpAcceptConnection(file.fileno(), blocking)

        if http_ptr == _ffi.NULL:
            raise ConnectionError(f"Failed to accept connection on {path=}")

        return cls(http_ptr)

    @property
    def address(self) -> HttpAddr:
        """Return the address of the CUPS server."""
        return HttpAddr(_lib.httpGetAddress(self.ffi_value))

    @property
    def authString(self) -> str:
        """Return the authentication string used for the connection."""
        return _bytes_to_value(_lib.httpGetAuthString(self.ffi_value))

    @property
    def blocking(self) -> bool:
        """Return whether the connection is blocking."""
        return bool(_bytes_to_value(_lib.httpGetBlocking(self.ffi_value)))

    @blocking.setter
    def blocking(self, value: bool) -> None:
        """Set whether the connection is blocking."""
        _lib.httpSetBlocking(self.ffi_value, value)

    @property
    def contentEncoding(self) -> str:
        """Return the content encoding used for the connection."""
        return _bytes_to_value(_lib.httpGetContentEncoding(self.ffi_value))

    @property
    def cookie(self) -> str:
        """Return the cookies used for the connection."""
        return _bytes_to_value(_lib.httpGetCookies(self.ffi_value))

    @cookie.setter
    def cookie(self, value: str) -> None:
        """Set the cookies for the connection."""
        if not value:
            _lib.httpClearCookie(self.ffi_value)
            return

        c_cookie = _value_to_bytes(value)
        _lib.httpSetCookie(self.ffi_value, c_cookie)

    @property
    def credentials(self) -> str:
        """Return the credentials used for the connection."""
        return _bytes_to_value(_lib.httpCopyPeerCredentials(self.ffi_value))

    @classmethod
    def connect(
        cls,
        *,
        host: str = getServer(),
        port: int = getPort(),
        addr_family: socket.AddressFamily = socket.AF_UNSPEC,
        encryption: HttpEncryption = getEncryption(),
        blocking: bool = True,
        msec: int = 3000,
    ) -> "Http":
        """Connect to a HTTP server."""
        http_ptr = _lib.httpConnect(
            _value_to_bytes(host),
            port,
            _ffi.NULL,
            addr_family.value,
            encryption.value,
            blocking,
            msec,
            _ffi.NULL,
        )

        if http_ptr == _ffi.NULL:
            raise ConnectionError(f"Failed to connect to {host}:{port}")

        return cls(http_ptr)

    def connctAgain(self, *, msec: int, cancel: bool) -> bool:
        """Attempt to reconnect the HTTP connection."""
        if self.ffi_value != _ffi.NULL:
            return bool(
                _bytes_to_value(_lib.httpConnectAgain(self.ffi_value, msec, cancel))
            )
        return False

    @classmethod
    def connectURI(
        cls,
        uri: str,
        host: str,
        hsize: int,
        port: int,
        resource: str,
        rsize: int,
        msec: int,
        cancel: int,
        *,
        blocking: bool,
        require_ca: bool,
    ) -> "Http":
        """Connect to a HTTP server using a URI."""
        http_ptr = _lib.httpConnectURI(
            _value_to_bytes(uri),
            _value_to_bytes(host),
            hsize,
            port,
            _value_to_bytes(resource),
            rsize,
            msec,
            cancel,
            blocking,
            require_ca,
            _ffi.NULL,
        )

        if http_ptr == _ffi.NULL:
            raise ConnectionError(f"Failed to connect to URI {uri}")

        return cls(http_ptr)

    @property
    def encryption(self) -> HttpEncryption:
        """Return the encryption type used for the connection."""
        return HttpEncryption(_bytes_to_value(_lib.httpGetEncryption(self.ffi_value)))

    @encryption.setter
    def encryption(self, encryption: HttpEncryption) -> None:
        """Set encryption mode for the connection.

        Args:
            encryption: Encryption mode to use

        Returns:
            True on success, False on failure

        """
        res = _lib.httpSetEncryption(self.ffi_value, encryption.value)
        if not res:
            raise ValueError(f"Failed to set {encryption=}")

    def flush(self):
        """Flush the HTTP connection."""
        if self.ffi_value != _ffi.NULL:
            _lib.httpFlush(self.ffi_value)

    def flushWrite(self) -> int:
        """Flush the write buffer of the HTTP connection."""
        if self.ffi_value != _ffi.NULL:
            return _lib.httpFlushWrite(self.ffi_value)
        return -1

    def getActivity(self) -> datetime:
        """Return the last activity time of the HTTP connection."""
        if self.ffi_value != _ffi.NULL:
            timestamp = _lib.httpGetActivity(self.ffi_value)
            return datetime.fromtimestamp(timestamp)
        return None

    def getField(self, field: HttpField) -> str:
        """Get a field value from a request/response."""
        return str(_bytes_to_value(_lib.httpGetField(self.ffi_value, field.value)))

    def gets(self, length: int = 1024) -> str:
        """Get a line of text from the HTTP connection."""
        buf = _ffi.new("char[]", length)
        return _bytes_to_value(_lib.httpGets(self.ffi_value, buf, length))

    @property
    def hostname(self) -> str:
        """Return the FQDN for the connection or local system."""
        slen = 256
        s = _ffi.new("char[]", slen)
        return str(_lib.httpGetHostname(self.ffi_value, s, slen))

    @property
    def is_chunked(self) -> bool:
        """Report whether a message body is chunked."""
        return bool(_bytes_to_value(_lib.httpIsChunked(self.ffi_value)))

    @property
    def is_encrypted(self) -> bool:
        """Report whether the connection is encrypted."""
        return bool(_bytes_to_value(_lib.httpIsEncrypted(self.ffi_value)))

    @property
    def keepAlive(self) -> bool:
        """Get the current Keep-Alive state of the connection."""
        return bool(_bytes_to_value(_lib.httpGetKeepAlive(self.ffi_value)))

    @keepAlive.setter
    def keepAlive(self, keep_alive: bool) -> None:
        """Set the Keep-Alive state of the connection.

        Args:
            keep_alive: True to enable Keep-Alive, False to disable

        """
        _lib.httpSetKeepAlive(self.ffi_value, keep_alive)

    @property
    def length(self) -> int:
        return _bytes_to_value(_lib.httpGetLength(self.ffi_value))

    @length.setter
    def length(self, length: int) -> None:
        """Set the content length for the next request."""
        _lib.httpSetLength(self.ffi_value, length)

    @property
    def pending(self) -> int:
        return _bytes_to_value(_lib.httpGetPending(self.ffi_value))

    @property
    def ready(self) -> int:
        return _bytes_to_value(_lib.httpGetReady(self.ffi_value))

    @property
    def remaining(self) -> int:
        """Get the number of remaining bytes in the message body or current chunk."""
        return _bytes_to_value(_lib.httpGetRemaining(self.ffi_value))

    @property
    def state(self) -> HttpState:
        """Get the current state of the HTTP request."""
        return HttpState(_bytes_to_value(_lib.httpGetState(self.ffi_value)))

    @property
    def status(self) -> HttpStatus:
        """Get the current HTTP status code of the connection."""
        return HttpStatus(_bytes_to_value(_lib.httpGetStatus(self.ffi_value)))

    def setAuthString(self, scheme: Optional[str], data: Optional[str]) -> None:
        """Set the current authorization string.

        Args:
            scheme: Auth scheme (None to clear it)
            data: Auth data (None for none)

        Note:
            You must still call httpSetField to set HTTP_FIELD_AUTHORIZATION
            prior to issuing a HTTP request using httpWriteRequest.

        """
        c_scheme = _value_to_bytes(scheme) if scheme else _ffi.NULL
        c_data = _value_to_bytes(data) if data else _ffi.NULL
        _lib.httpSetAuthString(self.ffi_value, c_scheme, c_data)

    def setDefaultField(self, field: HttpField, value: str) -> None:
        """Set the default value for a header field.

        Args:
            field: HTTP field to set
            value: Value to set

        """
        c_value = _value_to_bytes(value)
        _lib.httpSetDefaultField(self.ffi_value, field.value, c_value)

    def setField(self, field: HttpField, value: str) -> None:
        """Set a header field value.

        Args:
            field: HTTP field to set
            value: Value to set

        """
        c_value = _value_to_bytes(value)
        _lib.httpSetField(self.ffi_value, field.value, c_value)

    def setTimeout(self, timeout: float, cb=None, user_data=None) -> None:
        """Set timeout for the connection.

        Args:
            timeout: Timeout in seconds
            cb: Callback function (optional)
            user_data: User data for callback (optional)

        """
        _lib.httpSetTimeout(self.ffi_value, timeout, cb, user_data)

    def shutdown(self) -> None:
        """Shutdown the HTTP connection."""
        _lib.httpShutdown(self.ffi_value)

    def close(self) -> None:
        """Close the HTTP connection."""
        _lib.httpClose(self.ffi_value)

    def clearFields(self) -> None:
        """Clear all HTTP header fields."""
        _lib.httpClearFields(self.ffi_value)

    @property
    def error(self) -> int:
        """Get the last error on the connection."""
        return _lib.httpGetError(self.ffi_value)

    @property
    def expect(self) -> HttpStatus:
        """Get the expected status."""
        return HttpStatus(_bytes_to_value(_lib.httpGetExpect(self.ffi_value)))

    @expect.setter
    def expect(self, expect: HttpStatus) -> None:
        """Set the Expect header value.

        Args:
            expect: Expected status

        """
        _lib.httpSetExpect(self.ffi_value, expect.value)

    @property
    def fd(self) -> int:
        """Get the file descriptor for the connection."""
        return _lib.httpGetFd(self.ffi_value)

    def getSubField(self, field: HttpField, name: str) -> str:
        """Get a sub-field value from a header.

        Args:
            field: HTTP field to query
            name: Sub-field name

        Returns:
            Sub-field value as string

        """
        c_name = _value_to_bytes(name)
        c_value = _ffi.new("char[]", 256)
        result = _lib.httpGetSubField(self.ffi_value, field.value, c_name, c_value, 256)
        if result == _ffi.NULL:
            return ""
        return _bytes_to_value(result)

    def peek(self, length: int) -> str:
        """Peek at data in the connection buffer.

        Args:
            length: Maximum number of bytes to peek

        Returns:
            Peeked data as string

        """
        c_buffer = _ffi.new("char[]", length)
        bytes_read = _lib.httpPeek(self.ffi_value, c_buffer, length)
        if bytes_read < 0:
            return ""
        return _ffi.buffer(c_buffer, bytes_read)[:].decode()

    def printf(self, format_str: str, *args) -> int:
        """Print formatted data to the connection.

        Args:
            format_str: Format string
            *args: Arguments for format string

        Returns:
            Number of bytes written, or -1 on error

        """
        c_format = _value_to_bytes(format_str)
        return _lib.httpPrintf(self.ffi_value, c_format, *args)

    def read(self, length: int) -> str:
        """Read data from the connection.

        Args:
            length: Maximum number of bytes to read

        Returns:
            Data read as string

        """
        c_buffer = _ffi.new("char[]", length)
        bytes_read = _lib.httpRead(self.ffi_value, c_buffer, length)
        if bytes_read < 0:
            return ""
        return _ffi.buffer(c_buffer, bytes_read)[:].decode()

    def readRequest(self, resource: int = 1024) -> HttpState:
        """Read and parse a HTTP request.

        Args:
            resource: Size of resource buffer

        Returns:
            HTTP state after reading request

        """
        c_resource = _ffi.new("char[]", resource)
        state = _lib.httpReadRequest(self.ffi_value, c_resource, resource)
        return HttpState(state)

    def write(self, data: str) -> int:
        """Write data to the connection.

        Args:
            data: Data to write

        Returns:
            Number of bytes written, or -1 on error

        """
        c_data = _value_to_bytes(data)
        return _lib.httpWrite(self.ffi_value, c_data, len(c_data))

    def writeRequest(self, method: str, uri: str) -> bool:
        """Write a HTTP request.

        Args:
            method: HTTP method (GET, POST, etc.)
            uri: Request URI

        Returns:
            True on success, False on failure

        """
        c_method = _value_to_bytes(method)
        c_uri = _value_to_bytes(uri)
        return bool(_lib.httpWriteRequest(self.ffi_value, c_method, c_uri))

    def writeResponse(self, status: HttpStatus) -> bool:
        """Write a HTTP response.

        Args:
            status: HTTP status code

        Returns:
            True on success, False on failure

        """
        return bool(_lib.httpWriteResponse(self.ffi_value, status.value))

    def wait(self, msec: int) -> bool:
        """Wait for activity on the connection.

        Args:
            msec: Timeout in milliseconds

        Returns:
            True if activity occurred, False on timeout

        """
        return bool(_lib.httpWait(self.ffi_value, msec))

    def update(self) -> HttpStatus:
        """Update the HTTP state machine.

        Returns:
            HTTP status code

        """
        return HttpStatus(_lib.httpUpdate(self.ffi_value))

    def resolveHostname(self, buffer_size: int = 256) -> str:
        """Resolve the hostname for the connection.

        Args:
            buffer_size: Size of buffer for hostname

        Returns:
            Resolved hostname

        """
        c_buffer = _ffi.new("char[]", buffer_size)
        result = _lib.httpResolveHostname(self.ffi_value, c_buffer, buffer_size)
        return _bytes_to_value(result)

    @staticmethod
    def encode64(data: str, url: bool = False) -> str:
        """Base64 encode a string.

        Args:
            data: Data to encode
            url: If True, use URL-safe encoding

        Returns:
            Encoded string

        """
        c_data = _value_to_bytes(data)
        c_out = _ffi.new("char[]", len(c_data) * 2)
        outlen = len(c_data) * 2
        _lib.httpEncode64(c_out, outlen, c_data, len(c_data), url)
        return _bytes_to_value(c_out)

    @staticmethod
    def decode64(data: str) -> str:
        """Base64 decode a string.

        Args:
            data: Data to decode

        Returns:
            Decoded string

        """
        c_data = _value_to_bytes(data)
        c_out = _ffi.new("char[]", len(c_data))
        outlen = len(c_data)
        _lib.httpDecode64(c_out, _ffi.new("size_t *", outlen), c_data, _ffi.NULL)
        return _bytes_to_value(c_out)

    @staticmethod
    def getDateString(timestamp: datetime) -> str:
        """Convert a timestamp to a date string.

        Args:
            timestamp: Timestamp to convert

        Returns:
            Date string in HTTP format

        """
        c_s = _ffi.new("char[]", 64)
        time_t_val = int(timestamp.timestamp())
        _lib.httpGetDateString(time_t_val, c_s, 64)
        return _bytes_to_value(c_s)

    @staticmethod
    def getDateTime(date_str: str) -> datetime:
        """Convert a date string to a timestamp.

        Args:
            date_str: Date string in HTTP format

        Returns:
            Datetime object

        """
        c_date_str = _value_to_bytes(date_str)
        time_t_val = _lib.httpGetDateTime(c_date_str)
        return datetime.fromtimestamp(time_t_val)

    @classmethod
    def assembleURI(
        cls,
        scheme: str,
        username: Optional[str],
        host: str,
        port: int,
        resource: str,
        encoding: HttpUriCoding = HttpUriCoding.ALL,
    ) -> str:
        """Assemble a URI from its components.

        Args:
            scheme: URI scheme
            username: Username (optional)
            host: Hostname
            port: Port number
            resource: Resource path
            encoding: URI encoding flags

        Returns:
            Assembled URI

        """
        c_uri = _ffi.new("char[]", 1024)
        c_scheme = _value_to_bytes(scheme)
        c_username = _value_to_bytes(username) if username else _ffi.NULL
        c_host = _value_to_bytes(host)
        c_resource = _value_to_bytes(resource)

        status: HttpUriStatus = _lib.httpAssembleURI(
            encoding, c_uri, 1024, c_scheme, c_username, c_host, port, c_resource
        )

        if status == HttpUriStatus.OK:
            return _bytes_to_value(c_uri)
        raise ValueError(f"Failed to assemble URI: {status}")

    @classmethod
    def separateURI(cls, uri: str, decoding: HttpUriCoding = HttpUriCoding.ALL) -> dict:
        """Separate a URI into its components.

        Args:
            uri: URI to parse
            decoding: URI decoding flags

        Returns:
            Dictionary with scheme, username, host, port, resource

        """
        c_uri = _value_to_bytes(uri)
        c_scheme = _ffi.new("char[]", 256)
        c_username = _ffi.new("char[]", 256)
        c_host = _ffi.new("char[]", 256)
        c_resource = _ffi.new("char[]", 1024)
        c_port = _ffi.new("int *", 0)

        status = _lib.httpSeparateURI(
            decoding,
            c_uri,
            c_scheme,
            256,
            c_username,
            256,
            c_host,
            256,
            c_port,
            c_resource,
            1024,
        )

        return {
            "scheme": _bytes_to_value(c_scheme),
            "username": _bytes_to_value(c_username),
            "host": _bytes_to_value(c_host),
            "port": c_port[0],
            "resource": _bytes_to_value(c_resource),
            "status": status,
        }

    @staticmethod
    def assembleUUID(server: str, port: int, name: str, number: int) -> str:
        """Assemble a UUID string.

        Args:
            server: Server name
            port: Port number
            name: Resource name
            number: Unique number

        Returns:
            UUID string

        """
        c_server = _value_to_bytes(server)
        c_name = _value_to_bytes(name)
        c_buffer = _ffi.new("char[]", 128)

        _lib.httpAssembleUUID(c_server, port, c_name, number, c_buffer, 128)

        return _bytes_to_value(c_buffer)

    @staticmethod
    def resolveURI(
        uri: str, buffer_size: int = 1024, options: int = 0, cb=None, cb_data=None
    ) -> str:
        """Resolve a URI to its canonical form.

        Args:
            uri: URI to resolve
            buffer_size: Size of buffer for resolved URI
            options: Resolution options
            cb: Callback function (optional)
            cb_data: User data for callback (optional)

        Returns:
            Resolved URI

        """
        c_uri = _value_to_bytes(uri)
        c_resolved = _ffi.new("char[]", buffer_size)

        result = _lib.httpResolveURI(
            c_uri, c_resolved, buffer_size, options, cb, cb_data
        )

        return _bytes_to_value(result)
