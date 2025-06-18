from . import _cups
from typing import (
    Any,
    Dict,
    Optional,
    Tuple,
)
from .types import (
    cupsDest,
)

_ffi = _cups.ffi
_lib = _cups.lib


def addDests(
    name: str, instance: Optional[str], num_dests: int
) -> Tuple[int, cupsDest]:

    dests: cupsDest = cupsDest.cffi_new("**")
    c_name = _ffi.new("char[]", name.encode("utf-8"))
    c_instance = _ffi.new("char[]", instance.encode("utf-8")) if instance else _ffi.NULL
    count: int = _lib.cupsAddDest(
        c_name, c_instance, _ffi.cast("size_t", num_dests), dests.ffi_value
    )

    return count, dests


def copyDest(dest: cupsDest, num_dests: int) -> Tuple[int, Dict[str, cupsDest]]:
    dests: cupsDest = cupsDest.cffi_new("**")  # noqa # type: List[cupsDest]
    c_cupsDest = cupsDest.from_cffi(dest=dest)
    c_num_dests = _ffi.cast("size_t", num_dests)
    count: int = _lib.cupsCopyDest(c_cupsDest, c_num_dests, dests)

    return count, cupsDest.from_cffi_list(dests=dests, count=count)


def getDests() -> Dict[str, cupsDest]:

    dests: cupsDest = cupsDest.cffi_new("**")
    count: int = _lib.cupsGetDests(_ffi.NULL, dests.ffi_value)

    return cupsDest.from_cffi_list(dests=dests, count=count)


def getDestWithURI(name: str, uri: str) -> cupsDest:
    dest: Any = _lib.cupsGetDestWithURI(
        _ffi.new("char[]", name),
        _ffi.new("char[]", uri),
    )
    return cupsDest.from_cffi(dest=dest)


def setDests(num_dests: int, cups_dests_ffi: Any, http=None):
    _lib.cupsSetDests(_ffi.NULL, _ffi.cast("size_t", num_dests), cups_dests_ffi)
