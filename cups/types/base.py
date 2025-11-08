# Base class for all the types of CUPs

from abc import ABC
from functools import singledispatchmethod
from typing import Any

from cups import _cups

_ffi = _cups.ffi
_lib = _cups.lib


class cupsBaseClass(ABC):
    ffi_name: str
    ffi_free: str
    ffi_value: Any

    @singledispatchmethod
    def __init__(self, arg: Any = None) -> "cupsBaseClass":
        if arg is None:
            self.ffi_value = _ffi.new(f"{self.ffi_name} *")
        else:
            raise NotImplementedError

    @__init__.register
    def _(self, arg: str):
        self.ffi_value = _ffi.new(f"{self.ffi_name} {arg}")

    @__init__.register(_ffi.CData)
    def _(self, arg: Any):
        if arg and self._is_valid_ctype(arg):
            self.ffi_value = arg
        else:
            raise TypeError(
                f"Invalid CFFI type for {self.__class__.__name__}: {type(arg)}"
            )

    # @__init__.register(type(None))
    # def _(self, arg: None = None):
    #     self.ffi_value = _ffi.new(f"{self.ffi_name} *")

    # def __del__(self, extra_args: Optional[List] = None):
    #     if self.ffi_free:
    #         cffi_free = getattr(_lib, self.ffi_free, None)
    #         if cffi_free is None:
    #             raise AttributeError(f"C function '{self.ffi_free}' not found in lib")
    #         try:
    #             cffi_free(*extra_args) if extra_args else cffi_free()
    #         except Exception as e:
    #             raise RuntimeError(f"Failed to call C function '{self.ffi_free}': {e}")

    # @classmethod
    # def cffi_free(cls, extra_args: Optional[List]):
    #     if not cls.ffi_free:
    #         return

    #     cffi_free = getattr(_lib, cls.ffi_free, None)
    #     if cffi_free is None:
    #         raise AttributeError(f"C function '{cls.ffi_free}' not found in lib")

    #     try:
    #         cffi_free(*extra_args) if extra_args else cffi_free()
    #     except Exception as e:
    #         raise RuntimeError(f"Failed to call C function '{cls.ffi_free}': {e}")

    @property
    def valid(self):
        return self._is_valid_ctype(self.ffi_value)

    @classmethod
    def _is_valid_c_list(cls, ffi_value: Any) -> bool:
        try:
            ctype = _ffi.typeof(ffi_value)
            return ctype.item.kind == "pointer"
        except:
            return False

    @classmethod
    def _is_valid_ctype(cls, ffi_value: Any) -> bool:
        try:
            ctype = _ffi.typeof(ffi_value)
            ctype_name = _ffi.getctype(cls.ffi_name)

            if ctype.kind == "pointer":
                return ctype.item.cname == ctype_name
            return ctype.cname == _ffi.getctype(cls.ffi_name)
        except:
            return False

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__class__.__name__}(ffi_value={self.ffi_value})"
