from cups import _cups
from dataclasses import dataclass, field

from typing import Any, ClassVar, List, Optional, override

_ffi = _cups.ffi
_lib = _cups.lib


@dataclass
class cupsBaseClass:
    ffi_name: ClassVar[str]
    ffi_free: ClassVar[str]
    ffi_value: Any = field(repr=False)

    def cffi_new(self, extra_args: Optional[str] = None) -> "cupsBaseClass":
        ffi_struct: str = f"{self.ffi_name} {extra_args}" if extra_args else self.ffi_name
        self.ffi_value = _ffi.new(ffi_struct)
        return self

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

    @override
    def __repr__(self):
        return f"{self.__class__.__name__}({self.ffi_value})"
