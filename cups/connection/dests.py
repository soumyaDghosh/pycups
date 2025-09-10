from typing import Any, Optional  # noqa: D100

from cups import _cups
from cups.enums.cups import CUPSDestFlags
from cups.types.cups import cupsDest, cupsDestInfo
from cups.utils import _bytes_to_value

from .base import _Base

_ffi = _cups.ffi
_lib = _cups.lib


class DestsMixin(_Base):  # noqa: D101
    http: Any

    def addDest(self, name: str, instance: Optional[str] = None) -> dict[str, cupsDest]:  # noqa: D102, N802
        dests = self.getDests()
        c_name = _ffi.new("char[]", name.encode("utf-8"))
        c_instance = (
            _ffi.new("char[]", instance.encode("utf-8")) if instance else _ffi.NULL
        )
        c_dests = cupsDest.to_cffi_list(dests)
        count = _lib.cupsAddDest(c_name, c_instance, len(dests), c_dests)
        return cupsDest.from_cffi_list(dests=c_dests, count=count)

    def getDefault(self) -> str:  # noqa: D102, N802
        return _bytes_to_value(_lib.cupsGetDefault(self.http))  # type: ignore[return-value]

    def getDests(self) -> dict[str, cupsDest]:  # noqa: D102, N802
        dests: cupsDest = cupsDest("**")
        count: int = _lib.cupsGetDests(self.http, dests.ffi_value)

        return cupsDest.from_cffi_list(dests=dests, count=count)

    def setDests(self, dests: list[cupsDest]) -> bool:  # noqa: D102, N802
        return _bytes_to_value(  # type: ignore[return-value]
            _lib.cupsSetDests(self.http, len(dests), cupsDest.to_cffi_list(dests))  # type: ignore[arg-type]
        )

    def copyDestInfo(  # noqa: D102, N802
        self, dest: cupsDest, flags: CUPSDestFlags = CUPSDestFlags.NONE
    ) -> cupsDestInfo:
        return cupsDestInfo(
            _lib.cupsCopyDestInfo(self.http, dest.ffi_value, flags.value)
        )

    def checkDestSupported(  # noqa: D102, N802
        self,
        dest: cupsDest,
        dinfo: cupsDestInfo,
        option: str,
        value: Optional[str] = None,
    ) -> bool:
        return bool(
            _bytes_to_value(
                _lib.cupsCheckDestSupported(
                    self.http,
                    dest.ffi_value,
                    dinfo.ffi_value,
                    option.encode(),
                    value.encode() if value else _ffi.NULL,
                )
            )
        )
