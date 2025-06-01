from . import _cups
from dataclasses import (
    dataclass,
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
)

_ffi = _cups.ffi
_lib = _cups.lib


@dataclass
class cupsBaseClass:
    ffi_name: ClassVar[str]
    ffi_free: ClassVar[str]
    ffi_value: ClassVar[Any]

    @classmethod
    # This method actually returns a CData
    def cffi_new(cls, extra_args: Optional[str] = None) -> Any:
        ffi_struct: str = f"{cls.ffi_name} {extra_args}" if extra_args else cls.ffi_name
        cls.ffi_value = _ffi.new(ffi_struct)
        return cls

    @classmethod
    def cffi_free(cls, extra_args: Optional[List]):
        if not cls.ffi_free:
            return

        cffi_free = getattr(_lib, cls.ffi_free, None)
        if cffi_free is None:
            raise AttributeError(f"C function '{cls.ffi_free}' not found in lib")

        try:
            cffi_free(*extra_args) if extra_args else cffi_free()
        except Exception as e:
            raise RuntimeError(f"Failed to call C function '{cls.ffi_free}': {e}")


@dataclass
class cupsOption(cupsBaseClass):
    name: str
    value: Optional[Any]

    def to_dict(self) -> dict:
        return {"name": self.name, "value": self.value}


@dataclass
class cupsDest(cupsBaseClass):
    name: str
    instance: Optional[str]
    is_default: bool
    options: Dict[str, cupsOption]

    ffi_name = "cups_dest_t"
    ffi_free = "cupsFreeDests"
