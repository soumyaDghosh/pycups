from collections.abc import Mapping
from typing import Any, Dict, Optional

from cups.enums.ipp import IPPOp, IPPTag
from cups.types import Http
from cups.types.base import _ffi, _lib, cupsBaseClass
from cups.types.ipp import IPPAttribute, IPPRequest
from cups.utils import _bytes_to_value

from .option import cupsOption


class cupsDest(cupsBaseClass):
    @property
    def name(self) -> str:
        return str(_bytes_to_value(self.ffi_value.name))

    @property
    def instance(self) -> Optional[str]:
        return _bytes_to_value(self.ffi_value.instance)

    @property
    def options(self) -> Dict[str, cupsOption]:
        return cupsOption.from_cffi_list(
            opts=self.ffi_value.options, count=self.ffi_value.num_options
        )

    @property
    def is_default(self) -> bool:
        return self.ffi_value.is_default

    ffi_name = "cups_dest_t"
    ffi_free = "cupsFreeDests"

    @classmethod
    def connectDest(cls, *, dest: "cupsDest", flags, msec: int) -> Mapping[Http, str]:
        c_resource = _ffi.new("char[]", 256)
        http = _lib.cupsConnectDest(
            dest.ffi_value,
            flags,
            msec,
            _ffi.NULL,
            c_resource,
            256,
            _ffi.NULL,
            _ffi.NULL,
        )
        return {Http(http): _bytes_to_value(c_resource)}

    @classmethod
    def from_cffi_list(cls, dests: "cupsDest", count: int) -> "Dict[str, cupsDest]":
        """Convert a list of CFFI dest structs to a list of python cupsDest.

        Args:
            dests (Any): The CFFI *cups_dest_t pointer to a pointer.
            count (int): The number of destinations in the list.

        Returns:
            Dict[str, cupsDest]: The list of cupsDest.

        """
        results: Dict[str, cupsDest] = {}
        for i in range(count):
            new_dest: Any = dests.ffi_value[0][i]
            results[str(_bytes_to_value(new_dest.name))] = cupsDest.from_cffi(
                dest=new_dest
            )

        return results

    @classmethod
    def from_cffi(cls, dest: Any) -> "cupsDest":
        """Convert a single CFFI dest struct to a Python cupsDest object.

        Args:
            dest (Any): The CFFI cups_dest_t struct.

        Returns:
            cupsDest: The equivalent Python object.

        """
        return cls(dest)

    @classmethod
    def to_cffi_list(cls, dests: "Dict[str, cupsDest]") -> Any:
        count = len(dests)
        c_dests = _ffi.new(f"cups_dest_t[{count}]")

        for i, dest in enumerate(dests.values()):
            c_dests[i].name = _ffi.new("char[]", dest.name.encode())
            c_dests[i].instance = _ffi.new(
                "char[]",
                dest.instance.encode() if dest.instance is not None else b"",
            )
            c_dests[i].is_default = dest.is_default
            c_dests[i].num_options = len(dest.options)
            c_dests[i].options = cupsOption.to_cffi_list(dest.options)

        if cls._is_valid_c_list(c_dests):
            return c_dests
        return None

    def getPrinterAttributes(self, http: Any) -> dict[str, IPPAttribute]:
        ctype = _ffi.typeof(http)
        if ctype.kind != "pointer" and ctype.cname != "struct _http_s *":
            raise TypeError("http must be of type struct _http_s *")

        req: IPPRequest = IPPRequest(IPPOp.GET_PRINTER_ATTRIBUTES)
        req.addString(
            group=IPPTag.OPERATION,
            value_tag=IPPTag.URI,
            name="printer-uri",
            value=self.options["printer-uri-supported"].value,
        )
        res: IPPRequest = IPPRequest(_lib.cupsDoRequest(http, req.ffi_value, b"/"))
        if res is not None:
            return {
                attr.name: attr
                for attr in res.attributes
                if isinstance(attr, IPPAttribute)
            }

    def __str__(self):
        return f"{self.name} (Default)" if self.is_default else self.name
