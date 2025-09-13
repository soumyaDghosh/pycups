from cups.types.base import cupsBaseClass, _lib, _ffi
from cups.utils import _bytes_to_value
from typing import Any, Dict, Optional
from cups.types.ipp import IPPRequest, IPPTag, IPPAttribute

class cupsOption(cupsBaseClass):
    @property
    def name(self) -> str:
        return _bytes_to_value(self.ffi_value.name)

    @property
    def value(self) -> Optional[Any]:
        return _bytes_to_value(self.ffi_value.value)

    ffi_name = "cups_option_t"

    def to_dict(self) -> dict:
        return {"name": self.name, "value": self.value}

    def toAttribute(self, ipp_req: IPPRequest, group_tag: IPPTag) -> IPPAttribute:
        """Convert this cupsOption into an IPPAttribute.
        Args:
            ipp_req (IPPRequest): The IPPRequest to add the attribute to.
            group_tag (IPPTag): The group tag to use for the attribute.

        Returns:
            IPPAttribute: The created IPPAttribute.
        """

        return IPPAttribute(_lib.cupsEncodeOption(ipp_req.ffi_value, group_tag, self.name.encode(), self.value.encode() if self.value else b""))


    @classmethod
    def to_cffi_list(cls, opts: "Dict[str, cupsOption]") -> Any:
        count = len(opts)
        c_opts = _ffi.new(f"cups_option_t[{count}]")

        for i, opt in enumerate(opts.values()):
            c_opts[i].name = _ffi.new("char[]", opt.name.encode("utf-8"))
            c_opts[i].value = _ffi.new(
                "char[]",
                str(opt.value).encode("utf-8") if opt.value is not None else b"",
            )

        return c_opts

    @classmethod
    def from_cffi_list(cls, opts: Any, count: int) -> "Dict[str, cupsOption]":
        """
        Convert a list of CFFI dest structs to a list of python cupsOption.

        Args:
            dests (Any): The CFFI *cups_option_t pointer.

        Returns:
            List[cupsOption]: The list of cupsDest.
        """
        results: Dict[str, cupsOption] = {}
        for i in range(count):
            new_opt: Any = opts[i]
            results[str(_bytes_to_value(new_opt.name))] = cupsOption(new_opt)

        return results

    def __str__(self):
        return f"{self.name}: {self.value})"
