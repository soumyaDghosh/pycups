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

from .utils import (
    _bytes_to_value,
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

    @classmethod
    def from_cffi(cls, opt: Any) -> "cupsOption":
        """
        Convert a single CFFI dest struct to a Python cupsOption object.

        Args:
            dest (Any): The CFFI cups_option_t struct.

        Returns:
            cupsOption: The equivalent Python object.
        """
        opt_name: str = str(_bytes_to_value(opt.name))
        opt_value: Optional[str] = _bytes_to_value(opt.value)
        return cls(
            name=opt_name,
            value=opt_value,
        )


@dataclass
class cupsDest(cupsBaseClass):
    name: str
    instance: Optional[str]
    is_default: bool
    options: Dict[str, cupsOption]

    ffi_name = "cups_dest_t"
    ffi_free = "cupsFreeDests"

    @classmethod
    def from_cffi_list(cls, dests: Any, count: int) -> "Dict[str, cupsDest]":
        """
        Convert a list of CFFI dest structs to a list of python cupsDest.

        Args:
            dests (Any): The CFFI *cups_dest_t pointer.

        Returns:
            List[cupsDest]: The list of cupsDest.
        """
        results: Dict[str, cupsDest] = {}
        for i in range(count):
            new_dest: Any = dests.ffi_value[0][i]
            results[str(_bytes_to_value(new_dest.name))] = cupsDest.from_cffi(
                dest=new_dest
            )

        cls.cffi_free([count, dests.ffi_value[0]])

        return results

    @classmethod
    def from_cffi(cls, dest: Any) -> "cupsDest":
        """
        Convert a single CFFI dest struct to a Python cupsDest object.

        Args:
            dest (Any): The CFFI cups_dest_t struct.

        Returns:
            cupsDest: The equivalent Python object.
        """
        dest_name: str = str(_bytes_to_value(dest.name))
        dest_instance: Optional[str] = _bytes_to_value(dest.instance)
        is_default: bool = bool(dest.is_default)

        opts: Dict[str, cupsOption] = {}
        for j in range(dest.num_options):
            opt: Any = dest.options[j]
            opts[str(_bytes_to_value(opt.name))] = cupsOption.from_cffi(opt=opt)

        return cls(
            name=dest_name, instance=dest_instance, is_default=is_default, options=opts
        )
