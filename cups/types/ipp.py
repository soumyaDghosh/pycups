import struct  # noqa: D100
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, ClassVar, Optional, Union, override

from cups.enums.ipp import IPPOp, IPPRes, IPPState, IPPStatus, IPPTag
from cups.utils import _bytes_to_value

from .base import _ffi, _lib, cupsBaseClass


class IPPAttribute(cupsBaseClass):  # noqa: D101
    ffi_name: ClassVar[str] = "ipp_attribute_t"
    """
    https://openprinting.github.io/cups/libcups/cupspm.html#ippDeleteAttribute
    The doc says: "Delete a single attribute in an IPP message."
    Note: There is no way to actually delete a single attribute.
    """
    ffi_free: ClassVar[str] = "ippDeleteAttributes"

    @property
    def name(self) -> str:  # noqa: D102
        c_name = _lib.ippGetName(self.ffi_value)
        if c_name == _ffi.NULL:
            return ""
        return str(_bytes_to_value(c_name))

    @property
    def group_tag(self) -> int:  # noqa: D102
        return _lib.ippGetGroupTag(self.ffi_value)

    @property
    def value_tag(self) -> IPPTag:  # noqa: D102
        return IPPTag(_lib.ippGetValueTag(self.ffi_value))

    @property
    def count(self) -> int:  # noqa: D102
        return _lib.ippGetCount(self.ffi_value)

    @property
    def values(self) -> list[Any]:  # noqa: D102, PLR0911
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

    def __str__(self) -> str:
        required_size = _lib.ippAttributeString(self.ffi_value, _ffi.NULL, 0) + 1
        buffer = _ffi.new("char[]", required_size)
        _lib.ippAttributeString(self.ffi_value, buffer, required_size)
        return str(_bytes_to_value(buffer))


class IPPRequest(cupsBaseClass):  # noqa: D101
    ffi_name: ClassVar[str] = "ipp_t"

    def __init__(self, arg: Optional[Union[IPPOp, Any]] = None) -> None:  # noqa: ANN401
        if isinstance(arg, IPPOp):
            self.ffi_value = _lib.ippNewRequest(arg)

        elif arg and self._is_valid_ctype(arg):
            self.ffi_value = arg

        elif not arg:
            self.ffi_value = _lib.ippNew()

        else:
            raise ValueError("Invalid arguments passed")  # noqa: TRY003

    @property
    def attributes(self) -> list[IPPAttribute]:  # noqa: D102
        attrs: list[IPPAttribute] = []
        attr = _lib.ippGetFirstAttribute(self.ffi_value)
        while attr != _ffi.NULL:
            attrs.append(IPPAttribute(attr))
            attr = _lib.ippGetNextAttribute(self.ffi_value)
        return attrs

    @property
    def operation(self) -> IPPOp:  # noqa: D102
        return IPPOp(_lib.ippGetOperation(self.ffi_value))

    @property
    def state(self) -> IPPState:  # noqa: D102
        return IPPState(_lib.ippGetState(self.ffi_value))

    @property
    def statuscode(self) -> IPPStatus:  # noqa: D102
        return IPPStatus(_lib.ippGetStatusCode(self.ffi_value))

    @property
    def request_id(self) -> int:  # noqa: D102
        return _lib.ippGetRequestId(self.ffi_value)

    @property
    def version(self) -> float:  # noqa: D102
        minor = _ffi.new("int *")
        major = _lib.ippGetVersion(self.ffi_value, minor)
        return float(f"{major}.{minor[0]}")

    def __len__(self) -> int:
        return _lib.ippGetLength(self.ffi_value)

    def addString(  # noqa: D102, N802
        self,
        group: IPPTag,
        value_tag: IPPTag,
        name: str,
        value: str,
        language: Optional[str] = None,
    ) -> IPPAttribute:
        if group is None or value_tag is None or name is None or value is None:
            raise RuntimeError("Invalid parameters passed")  # noqa: TRY003

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

    def addStrings(  # noqa: ANN201, D102, N802
        self,
        group: IPPTag,
        value_tag: IPPTag,
        name: str,
        values: list[str],
        language: Optional[str] = None,
    ):
        if group is None or value_tag is None or name is None or values is None:
            raise RuntimeError("Invalid parameters passed")  # noqa: TRY003

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

    def setString(  # noqa: ANN201, D102, N802
        self,
        attr: IPPAttribute,
        position: int,
        value: str,
    ):
        if attr is None or position < 0 or value is None:
            raise RuntimeError("Invalid parameters passed")  # noqa: TRY003

        return IPPAttribute(
            _lib.ippSetString(self.ffi_value, attr.ffi_value, position, value.encode())
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(state={self.state})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(state={self.state}, statuscode={self.statuscode}, version={self.version})"


@dataclass
class IPPError(Exception):
    """Exception for IPP/CUPS request errors."""

    _response: IPPRequest = field(repr=False)

    @property
    def status(self) -> IPPStatus:  # noqa: D102
        return self._response.statuscode

    @property
    def message(self) -> str:  # noqa: D102
        return _bytes_to_value(_lib.ippGetErrorString(self.status))

    @override
    def __str__(self) -> str:
        return f"IPP Error {self.status.value} ({self.status.name}): {self.message}"
