from .base import cupsBaseClass, _lib, _ffi
from cups.utils import _bytes_to_value
from typing import Any, ClassVar, override
from dataclasses import dataclass, field
from cups.enums.ipp import IPPRes, IPPState, IPPStatus, IPPTag, IPPOp
from datetime import datetime
import struct


@dataclass
class IPPAttribute(cupsBaseClass):
    ffi_name: ClassVar[str] = "ipp_attribute_t"
    """
    From the docs
    https://openprinting.github.io/cups/libcups/cupspm.html#ippDeleteAttribute
    Delete a single attribute in an IPP message.
    There is no way to actually delete a single attribute.
    """
    ffi_free: ClassVar[str] = "ippDeleteAttributes"

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
        if self.value_tag in [IPPTag.INTEGER, IPPTag.ENUM, IPPTag.RANGE]:
            return [_lib.ippGetInteger(self.ffi_value, i) for i in range(self.count)]
        elif self.value_tag in [
            IPPTag.TEXT,
            IPPTag.NAME,
            IPPTag.KEYWORD,
            IPPTag.URI,
            IPPTag.MIMETYPE,
            IPPTag.CHARSET,
            IPPTag.LANGUAGE,
        ]:
            return [
                _bytes_to_value(_lib.ippGetString(self.ffi_value, i))
                for i in range(self.count)
            ]
        elif self.value_tag == IPPTag.BOOLEAN:
            return [_lib.ippGetBoolean(self.ffi_value, i) for i in range(self.count)]
        elif self.value_tag == IPPTag.DATE:
            dates: list[datetime] = []
            for i in range(self.count):
                date_hex_bytes: bytes = _ffi.string(_lib.ippGetDate(self.ffi_value, i))
                dates.append(datetime(*struct.unpack(">H5B", date_hex_bytes)))
            return dates
        elif self.value_tag == IPPTag.RESOLUTION:
            resolutions = []
            for i in range(self.count):
                unit = _ffi.new("ipp_res_t *")
                res = _ffi.new("int *")
                _lib.ippGetResolution(self.ffi_value, i, res, unit)
                resolutions.append((res[0], IPPRes(unit[0])))
            return resolutions
        else:
            return []


@dataclass
class IPPRequest(cupsBaseClass):
    ffi_name: ClassVar[str] = "ipp_t"

    @override
    @classmethod
    def cffi_new(cls, op: IPPOp) -> "IPPRequest":
        cls.ffi_value = _lib.ippNewRequest(op)
        return cls(ffi_value=cls.ffi_value)

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

    def addString(
        self,
        group: IPPTag,
        value_tag: IPPTag,
        name: str,
        value: str,
        language: str = None,
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


@dataclass
class IPPError(Exception):
    """
    Exception for IPP/CUPS request errors.
    """

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
