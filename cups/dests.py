from . import _cups
from typing import (
    Any,
    Dict,
    Optional,
    Tuple,
)
from .types import (
    cupsDest,
    cupsOption,
)

from .utils import (
    _bytes_to_value,
)

_ffi = _cups.ffi
_lib = _cups.lib


def addDests(name: str, instance: Optional[str], num_dests: int) -> Tuple[int, cupsDest]:

    dests: cupsDest = cupsDest.cffi_new("**")
    c_name = _ffi.new("char[]", name.encode("utf-8"))
    c_instance = _ffi.new("char[]", instance.encode("utf-8")) if instance else _ffi.NULL
    count: int = _lib.cupsAddDest(
        c_name,
        c_instance,
        _ffi.cast("size_t", num_dests),
        dests.ffi_value
    )

    return count, dests


def getDests() -> Dict[str, cupsDest]:

    dests: cupsDest = cupsDest.cffi_new("**")
    count: int = _lib.cupsGetDests(_ffi.NULL, dests.ffi_value)
    results: Dict[str, cupsDest] = {}
    for i in range(count):
        dest: Any = dests.ffi_value[0][i]
        dest_name: str = str(_bytes_to_value(dest.name))
        dest_instance: Optional[str] = _bytes_to_value(dest.instance)
        is_default: bool = bool(dest.is_default)
        opts: Dict[str, cupsOption] = {}
        for j in range(dest.num_options):
            opt: Any = dest.options[j]
            opt_name: str = str(_bytes_to_value(opt.name))
            opt_value: Optional[str] = _bytes_to_value(opt.value)
            opts[opt_name] = cupsOption(name=opt_name, value=opt_value)
        results[dest_name] = cupsDest(
            name=dest_name, instance=dest_instance, is_default=is_default, options=opts
        )

    cupsDest.cffi_free([count, dests.ffi_value[0]])
    return results

def setDests(num_dests: int, cups_dests_ffi: Any, http=None):
    _lib.cupsSetDests(_ffi.NULL, _ffi.cast("size_t", num_dests), cups_dests_ffi)


def getOption(name: str, options: Dict[str, cupsOption]) -> Optional[cupsOption]:
    return options[name]
