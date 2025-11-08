from pathlib import Path

from cups.enums import CUPSRasterMode, IPPOrient, IPPQuality
from cups.types.base import _lib, cupsBaseClass
from cups.types.media import cupsMedia
from cups.utils import _value_to_bytes

from .pageheader import cupsPageHeader


class cupsRaster(cupsBaseClass):
    ffi_name = "cups_raster_t"

    def initHeader(
        self,
        header: cupsPageHeader,
        media: cupsMedia,
        optimize: str,
        quality: IPPQuality,
        intent: str,
        orientation: IPPOrient,
        sides: list[str],
        type: str,
        xdpi: int,
        ydpi: int,
        sheet_back: str,
    ) -> bool:
        return bool(
            _lib.cupsRasterInitHeader(
                header.ffi_value,
                media.ffi_value,
                optimize.encode(),
                quality.value,
                intent.encode(),
                orientation.value,
                _value_to_bytes(sides),
                type.encode(),
                xdpi,
                ydpi,
                sheet_back.encode(),
            )
        )

    @classmethod
    def open(cls, file: Path, mode: CUPSRasterMode) -> "cupsRaster":
        return cupsRaster(_lib.cupsRasterOpen(file.open().fileno(), mode.value))

    def readHeader(self) -> cupsPageHeader:
        header = cupsPageHeader()
        ok = _lib.cupsRasterReadHeader(self.ffi_value, header.ffi_value)
        if not ok:
            raise RuntimeError("Failed to read raster header")
        return header

    def writeHeader(self, header: cupsPageHeader) -> None:
        ok = _lib.cupsRasterWriteHeader(self.ffi_value, header.ffi_value)
        return ok

    def close(self) -> None:
        _lib.cupsRasterClose(self.ffi_value)
