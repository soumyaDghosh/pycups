from cups import _cups
from cups.types.cups import cupsDest
from typing import Any, Dict
from cups.utils import _bytes_to_value

_ffi = _cups.ffi
_lib = _cups.lib


class DestsMixin:
    http: Any = None

    def getDefault(self) -> str:
        return _bytes_to_value(_lib.cupsGetDefault(self.http))

    def getDests(self) -> Dict[str, cupsDest]:
        dests: cupsDest = cupsDest.cffi_new("**")
        count: int = _lib.cupsGetDests(self.http, dests.ffi_value)

        return cupsDest.from_cffi_list(dests=dests, count=count)

    def setDests(self, num_dests: int, cups_dests_ffi: Any) -> bool:
        return _bytes_to_value(
            _lib.cupsSetDests(self.http, _ffi.cast("size_t", num_dests), cups_dests_ffi)
        )
