import struct
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Optional, Union, override

from cups.enums.ipp import IPPOp, IPPRes, IPPState, IPPStatus, IPPTag
from cups.types.http import Http
from cups.utils import _bytes_to_value, _value_to_bytes

from .base import _ffi, _lib, cupsBaseClass


class IPPAttribute(cupsBaseClass):
    ffi_name: str = "ipp_attribute_t"
    """
    https://openprinting.github.io/cups/libcups/cupspm.html#ippDeleteAttribute
    The doc says: "Delete a single attribute in an IPP message."
    Note: There is no way to actually delete a single attribute.
    """
    ffi_free: str = "ippDeleteAttributes"

    @property
    def credentials(self) -> str:
        c_credentials = _lib.ippCopyCredentialsString(self.ffi_value)
        return str(_bytes_to_value(c_credentials))

    @property
    def name(self) -> str:
        c_name = _lib.ippGetName(self.ffi_value)
        if c_name == _ffi.NULL:
            return ""
        return str(_bytes_to_value(c_name))

    @property
    def group_tag(self) -> int:
        return _lib.ippGetGroupTag(self.ffi_value)

    @property
    def value_tag(self) -> IPPTag:
        return IPPTag(_lib.ippGetValueTag(self.ffi_value))

    @property
    def count(self) -> int:
        return _lib.ippGetCount(self.ffi_value)

    @property
    def values(self) -> list[Any]:
        if self.value_tag in [
            IPPTag.ZERO,
            IPPTag.NOVALUE,
            IPPTag.NOTSETTABLE,
            IPPTag.ADMINDEFINE,
        ]:
            return []
        if self.value_tag == IPPTag.RANGE:
            ranges = []
            for i in range(self.count):
                upper = _ffi.new("int *")
                lower = _lib.ippGetRange(self.ffi_value, i, upper)
                ranges.append(range(lower, upper[0]))
            return ranges
        if self.value_tag in [IPPTag.INTEGER, IPPTag.ENUM]:
            return [_lib.ippGetInteger(self.ffi_value, i) for i in range(self.count)]
        if self.value_tag in [
            IPPTag.TEXT,
            IPPTag.NAME,
            IPPTag.KEYWORD,
            IPPTag.URI,
            IPPTag.MIMETYPE,
            IPPTag.CHARSET,
            IPPTag.LANGUAGE,
        ]:
            return [
                _bytes_to_value(_lib.ippGetString(self.ffi_value, i, _ffi.NULL))
                for i in range(self.count)
            ]
        if self.value_tag == IPPTag.BOOLEAN:
            return [_lib.ippGetBoolean(self.ffi_value, i) for i in range(self.count)]
        if self.value_tag == IPPTag.DATE:
            dates: list[datetime] = []
            for i in range(self.count):
                date_hex_bytes: bytes = _ffi.string(_lib.ippGetDate(self.ffi_value, i))
                dates.append(datetime(*struct.unpack(">H5B", date_hex_bytes)))
            return dates
        if self.value_tag == IPPTag.RESOLUTION:
            resolutions = []
            for i in range(self.count):
                unit = _ffi.new("ipp_res_t *")
                res = _ffi.new("int *")
                _lib.ippGetResolution(self.ffi_value, i, res, unit)
                resolutions.append((res[0], IPPRes(unit[0])))
            return resolutions
        if self.value_tag == IPPTag.BEGIN_COLLECTION:
            collections = []
            for i in range(self.count):
                attr = IPPRequest(_lib.ippGetCollection(self.ffi_value, i))
                collections.append(attr)
            return collections
        return []

    def setBoolean(self, ipp_req: "IPPRequest", value: bool) -> bool:
        attr_ptr = _ffi.new("ipp_attribute_t **")
        attr_ptr[0] = self.ffi_value

        ok = _lib.ippSetBoolean(ipp_req.ffi_value, attr_ptr, 0, bool(value))

        # Update our ffi_value in case the library created/changed the attribute.
        self.ffi_value = attr_ptr[0]
        return bool(_bytes_to_value(ok))

    def setDate(self, ipp_req: "IPPRequest", value: datetime) -> bool:
        attr_ptr = _ffi.new("ipp_attribute_t **")
        attr_ptr[0] = self.ffi_value

        date_bytes = struct.pack(
            ">H5B",
            value.year,
            value.month,
            value.day,
            value.hour,
            value.minute,
            value.second,
        )
        c_date = _ffi.new("char []", date_bytes)

        ok = _lib.ippSetDate(ipp_req.ffi_value, attr_ptr, 0, c_date)

        self.ffi_value = attr_ptr[0]
        return bool(_bytes_to_value(ok))

    def setInteger(self, ipp_req: "IPPRequest", value: int) -> bool:
        attr_ptr = _ffi.new("ipp_attribute_t **")
        attr_ptr[0] = self.ffi_value

        ok = _lib.ippSetInteger(ipp_req.ffi_value, attr_ptr, 0, value)

        self.ffi_value = attr_ptr[0]
        return bool(_bytes_to_value(ok))

    def setName(self, ipp_req: "IPPRequest", value: str) -> bool:
        attr_ptr = _ffi.new("ipp_attribute_t **")
        attr_ptr[0] = self.ffi_value

        ok = _lib.ippSetName(ipp_req.ffi_value, attr_ptr, 0, value.encode())

        self.ffi_value = attr_ptr[0]
        return bool(_bytes_to_value(ok))

    def __str__(self):
        required_size = _lib.ippAttributeString(self.ffi_value, _ffi.NULL, 0) + 1
        buffer = _ffi.new("char[]", required_size)
        _lib.ippAttributeString(self.ffi_value, buffer, required_size)
        return str(_bytes_to_value(buffer))


class IPPRequest(cupsBaseClass):
    ffi_name: str = "ipp_t"

    def __init__(self, arg: Optional[Union[IPPOp, Any]] = None):
        if isinstance(arg, IPPOp):
            self.ffi_value = _lib.ippNewRequest(arg)

        elif arg and self._is_valid_ctype(arg):
            self.ffi_value = arg

        elif not arg:
            self.ffi_value = _lib.ippNew()

        else:
            raise ValueError("Invalid arguments passed")

    @property
    def attributes(self) -> list[IPPAttribute]:
        attrs: list[IPPAttribute] = []
        attr = _lib.ippGetFirstAttribute(self.ffi_value)
        while attr != _ffi.NULL:
            attrs.append(IPPAttribute(attr))
            attr = _lib.ippGetNextAttribute(self.ffi_value)
        return attrs

    @property
    def operation(self) -> IPPOp:
        return IPPOp(_lib.ippGetOperation(self.ffi_value))

    @property
    def state(self) -> IPPState:
        return IPPState(_lib.ippGetState(self.ffi_value))

    @property
    def statuscode(self) -> IPPStatus:
        return IPPStatus(_lib.ippGetStatusCode(self.ffi_value))

    @property
    def request_id(self) -> int:
        return _lib.ippGetRequestId(self.ffi_value)

    @property
    def version(self) -> float:
        minor = _ffi.new("int *")
        major = _lib.ippGetVersion(self.ffi_value, minor)
        return float(f"{major}.{minor[0]}")

    def __len__(self) -> int:
        return _lib.ippGetLength(self.ffi_value)

    def addString(
        self,
        group: IPPTag,
        value_tag: IPPTag,
        name: str,
        value: str,
        language: Optional[str] = None,
    ) -> IPPAttribute:
        if group is None or value_tag is None or name is None or value is None:
            raise RuntimeError("Invalid parameters passed")

        language = _ffi.NULL if language is None else language.encode()

        return IPPAttribute(
            _lib.ippAddString(
                self.ffi_value,
                group,
                value_tag,
                name.encode(),
                language,
                value.encode(),
            )
        )

    def addStrings(
        self,
        group: IPPTag,
        value_tag: IPPTag,
        name: str,
        values: list[str],
        language: Optional[str] = None,
    ):
        if group is None or value_tag is None or name is None or values is None:
            raise RuntimeError("Invalid parameters passed")

        language = _ffi.NULL if language is None else language.encode()

        c_array = _ffi.new("char *[]", len(values))
        for i, value in enumerate(values):
            c_array[i] = _ffi.new("char[]", value.encode())

        return IPPAttribute(
            _lib.ippAddStrings(
                self.ffi_value,
                group,
                value_tag,
                name.encode(),
                len(values),
                language,
                c_array,
            )
        )

    def setString(
        self,
        attr: IPPAttribute,
        position: int,
        value: str,
    ):
        if attr is None or position < 0 or value is None:
            raise RuntimeError("Invalid parameters passed")

        return IPPAttribute(
            _lib.ippSetString(self.ffi_value, attr.ffi_value, position, value.encode())
        )

    def read(self, http: Http) -> IPPState:
        return IPPState(_lib.ippRead(http.ffi_value, self.ffi_value))

    def readFile(self, file: Path) -> IPPState:
        file_fd = file.open().fileno()
        return IPPState(_lib.ippReadFile(file_fd, self.ffi_value))

    def restore(self):
        _lib.ippRestore(self.ffi_value)

    def save(self):
        _lib.ippSave(self.ffi_value)

    def setValueTag(self, attr: IPPAttribute, value_tag: IPPTag):
        return bool(
            _lib.ippSetValueTag(self.ffi_value, attr.ffi_value, value_tag.value)
        )

    def write(self, http: Http) -> IPPState:
        return IPPState(_lib.ippWriteRequest(http.ffi_value, self.ffi_value))

    def writeFile(self, file: Path) -> IPPState:
        file_fd = file.open().fileno()
        return IPPState(_lib.ippWriteFile(file_fd, self.ffi_value))

    def __str__(self):
        return f"{self.__class__.__name__}(state={self.state})"

    def __repr__(self):
        return f"{self.__class__.__name__}(state={self.state}, statuscode={self.statuscode}, version={self.version})"


class IPPFile(cupsBaseClass):
    ffi_name: str = "ipp_file_t"

    def close(self) -> bool:
        ok = _lib.ippFileClose(self.ffi_value)
        if not ok:
            raise RuntimeError("Failed to close IPP file")
        return ok

    def expandVars(self, src: str) -> str:
        c_dest_size = len(src) * 4 + 1
        c_dest = _ffi.new("char []", c_dest_size)
        size = _lib.ippFileExpandVars(
            self.ffi_value, c_dest, _value_to_bytes(src), c_dest_size
        )
        return str(_bytes_to_value(c_dest[:size]))

    @property
    def fileName(self) -> str:
        c_name = _lib.ippFileGetFileName(self.ffi_value)
        return str(_bytes_to_value(c_name))

    def getAttribute(self, name: str, value_tag: IPPTag) -> IPPAttribute:
        return IPPAttribute(
            _lib.ippFileGetAttribute(
                self.ffi_value, _value_to_bytes(name), value_tag.value
            )
        )

    def getAttributes(self) -> IPPRequest:
        return IPPRequest(_lib.ippFileGetAttributes(self.ffi_value))

    def getVar(self, name: str) -> str:
        return str(
            _bytes_to_value(_lib.ippFileGetVar(self.ffi_value, _value_to_bytes(name)))
        )

    @property
    def lineNumber(self) -> int:
        return _lib.ippFileGetLineNumber(self.ffi_value)

    def readCollection(self) -> IPPRequest:
        return IPPRequest(_lib.ippFileReadCollection(self.ffi_value))

    def restorePosition(self) -> bool:
        return bool(_lib.ippFileRestorePosition(self.ffi_value))

    def savePosition(self) -> bool:
        return bool(_lib.ippFileSavePosition(self.ffi_value))

    def setAttributes(self, attrs: IPPRequest) -> bool:
        return bool(_lib.ippFileSetAttributes(self.ffi_value, attrs.ffi_value))

    def setGroupTag(self, group_tag: IPPTag) -> bool:
        return bool(_lib.ippFileSetGroupTag(self.ffi_value, group_tag.value))

    def setVar(self, name: str, value: str) -> bool:
        return bool(
            _lib.ippFileSetVar(
                self.ffi_value, _value_to_bytes(name), _value_to_bytes(value)
            )
        )

    @property
    def token(self) -> bool:
        c_token = _ffi.new("char []", 256)
        return bool(
            _bytes_to_value(_lib.ippFileReadToken(self.ffi_value, c_token, 256))
        )

    @token.setter
    def token(self, token: str) -> None:
        _lib.ippFileWriteToken(self.ffi_value, _value_to_bytes(token))


@dataclass
class IPPError(Exception):
    """Exception for IPP/CUPS request errors."""

    _response: IPPRequest = field(repr=False)

    @property
    def status(self) -> IPPStatus:
        return self._response.statuscode

    @property
    def message(self) -> str:
        return _bytes_to_value(_lib.ippGetErrorString(self.status))

    @override
    def __str__(self):
        return f"IPP Error {self.status.value} ({self.status.name}): {self.message}"
