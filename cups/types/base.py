from abc import ABC  # noqa: D100
from typing import Any, ClassVar

from cups import _cups

_ffi = _cups.ffi
_lib = _cups.lib


class cupsBaseClass(ABC):  # noqa: D101, N801
    ffi_name: ClassVar[str]
    ffi_free: ClassVar[str]
    ffi_value: Any

    def __init__(self, args=None) -> None:  # noqa: ANN001
        if args and self._is_valid_ctype(args):
            self.ffi_value = args
        elif isinstance(args, str):
            self.ffi_value = _ffi.new(f"{self.ffi_name} {args}")
        else:
            self.ffi_value = _ffi.new(f"{self.ffi_name} *")

    # def __del__(self, extra_args: Optional[List] = None):
    #     if self.ffi_free:
    #         cffi_free = getattr(_lib, self.ffi_free, None)  # noqa: ERA001
    #         if cffi_free is None:
    #             raise AttributeError(f"C function '{self.ffi_free}' not found in lib")  # noqa: ERA001
    #         try:  # noqa: ERA001
    #             cffi_free(*extra_args) if extra_args else cffi_free()  # noqa: ERA001
    #         except Exception as e:  # noqa: ERA001
    #             raise RuntimeError(f"Failed to call C function '{self.ffi_free}': {e}")  # noqa: ERA001

    # @classmethod
    # def cffi_free(cls, extra_args: Optional[List]):
    #     if not cls.ffi_free:
    #         return  # noqa: ERA001

    #     cffi_free = getattr(_lib, cls.ffi_free, None)  # noqa: ERA001
    #     if cffi_free is None:
    #         raise AttributeError(f"C function '{cls.ffi_free}' not found in lib")  # noqa: ERA001

    #     try:  # noqa: ERA001
    #         cffi_free(*extra_args) if extra_args else cffi_free()  # noqa: ERA001
    #     except Exception as e:  # noqa: ERA001
    #         raise RuntimeError(f"Failed to call C function '{cls.ffi_free}': {e}")  # noqa: ERA001

    @property
    def valid(self):  # noqa: ANN201, D102
        return self._is_valid_ctype(self.ffi_value)

    @classmethod
    def _is_valid_c_list(cls, ffi_value: Any) -> bool:  # noqa: ANN401
        try:
            ctype = _ffi.typeof(ffi_value)
            return ctype.item.kind == "pointer"  # noqa: TRY300
        except:  # noqa: E722
            return False

    @classmethod
    def _is_valid_ctype(cls, ffi_value: Any) -> bool:  # noqa: ANN401
        try:
            ctype = _ffi.typeof(ffi_value)
            ctype_name = _ffi.getctype(cls.ffi_name)

            if ctype.kind == "pointer":
                return ctype.item.cname == ctype_name
            return ctype.cname == _ffi.getctype(cls.ffi_name)
        except:  # noqa: E722
            return False

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(ffi_value={self.ffi_value})"
