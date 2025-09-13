from cups.types.base import cupsBaseClass, _ffi, _lib
from cups.utils import _bytes_to_value
from typing import Tuple

class cupsPageHeader(cupsBaseClass):
    ffi_name = "cups_page_header_t"

    @property
    def AdvanceDistance(self) -> int:
        return self.ffi_value.AdvanceDistance

    @property
    def AdvanceMedia(self) -> int:
        return self.ffi_value.AdvanceMedia

    @property
    def Collate(self) -> bool:
        return bool(self.ffi_value.Collate)

    @property
    def CutMedia(self) -> int:
        return self.ffi_value.CutMedia

    @property
    def Duplex(self) -> bool:
        return bool(self.ffi_value.Duplex)

    @property
    def HWResolution(self) -> Tuple[int, int]:
        return (self.ffi_value.HWResolution[0], self.ffi_value.HWResolution[1])

    @property
    def ImagingBoundingBox(self) -> Tuple[int, int, int, int]:
        return Tuple(self.ffi_value.ImagingBoundingBox[i] for i in range(4))

    @property
    def InsertSheet(self) -> bool:
        return bool(self.ffi_value.InsertSheet)

    @property
    def Jog(self) -> int:
        return self.ffi_value.Jog

    @property
    def LeadingEdge(self) -> int:
        return self.ffi_value.LeadingEdge

    @property
    def ManualFeed(self) -> bool:
        return bool(self.ffi_value.ManualFeed)

    @property
    def Margins(self) -> tuple[int, int]:
        return (self.ffi_value.Margins[0], self.ffi_value.Margins[1])

    @property
    def MediaClass(self) -> str:
        return _bytes_to_value(self.ffi_value.MediaClass)

    @property
    def MediaColor(self) -> str:
        return _bytes_to_value(self.ffi_value.MediaColor)

    @property
    def MediaPosition(self) -> int:
        return self.ffi_value.MediaPosition

    @property
    def MediaType(self) -> str:
        return _bytes_to_value(self.ffi_value.MediaType)

    @property
    def MediaWeight(self) -> int:
        return self.ffi_value.MediaWeight

    @property
    def MirrorPrint(self) -> bool:
        return bool(self.ffi_value.MirrorPrint)

    @property
    def NegativePrint(self) -> bool:
        return bool(self.ffi_value.NegativePrint)

    @property
    def NumCopies(self) -> int:
        return self.ffi_value.NumCopies

    @property
    def Orientation(self) -> int:
        return self.ffi_value.Orientation

    @property
    def OutputFaceUp(self) -> bool:
        return bool(self.ffi_value.OutputFaceUp)

    @property
    def OutputType(self) -> str:
        return _bytes_to_value(self.ffi_value.OutputType)

    @property
    def PageSize(self) -> tuple[int, int]:
        return (self.ffi_value.PageSize[0], self.ffi_value.PageSize[1])

    @property
    def Separations(self) -> bool:
        return bool(self.ffi_value.Separations)

    @property
    def TraySwitch(self) -> bool:
        return bool(self.ffi_value.TraySwitch)

    @property
    def Tumble(self) -> bool:
        return bool(self.ffi_value.Tumble)

    @property
    def cupsBitsPerColor(self) -> int:
        return self.ffi_value.cupsBitsPerColor

    @property
    def cupsBitsPerPixel(self) -> int:
        return self.ffi_value.cupsBitsPerPixel

    @property
    def cupsBorderlessScalingFactor(self) -> float:
        return self.ffi_value.cupsBorderlessScalingFactor

    @property
    def cupsBytesPerLine(self) -> int:
        return self.ffi_value.cupsBytesPerLine

    @property
    def cupsColorOrder(self) -> int:
        return self.ffi_value.cupsColorOrder

    @property
    def cupsColorSpace(self) -> int:
        return self.ffi_value.cupsColorSpace

    @property
    def cupsCompression(self) -> int:
        return self.ffi_value.cupsCompression

    @property
    def cupsHeight(self) -> int:
        return self.ffi_value.cupsHeight

    @property
    def cupsImagingBBox(self) -> tuple[float, float, float, float]:
        return tuple(self.ffi_value.cupsImagingBBox[i] for i in range(4))

    @property
    def cupsInteger(self) -> tuple[int, ...]:
        return tuple(self.ffi_value.cupsInteger[i] for i in range(16))

    @property
    def cupsMarkerType(self) -> str:
        return _bytes_to_value(self.ffi_value.cupsMarkerType)

    @property
    def cupsMediaType(self) -> int:
        return self.ffi_value.cupsMediaType

    @property
    def cupsNumColors(self) -> int:
        return self.ffi_value.cupsNumColors

    @property
    def cupsPageSizeName(self) -> str:
        return _bytes_to_value(self.ffi_value.cupsPageSizeName)

    @property
    def cupsPageSize(self) -> tuple[float, float]:
        return (self.ffi_value.cupsPageSize[0], self.ffi_value.cupsPageSize[1])

    @property
    def cupsReal(self) -> tuple[float, ...]:
        return tuple(self.ffi_value.cupsReal[i] for i in range(16))

    @property
    def cupsRenderingIntent(self) -> str:
        return _bytes_to_value(self.ffi_value.cupsRenderingIntent)

    @property
    def cupsRowCount(self) -> int:
        return self.ffi_value.cupsRowCount

    @property
    def cupsRowFeed(self) -> int:
        return self.ffi_value.cupsRowFeed

    @property
    def cupsRowStep(self) -> int:
        return self.ffi_value.cupsRowStep

    @property
    def cupsString(self) -> tuple[str, ...]:
        return tuple(_bytes_to_value(self.ffi_value.cupsString[i]) for i in range(16))

    @property
    def cupsWidth(self) -> int:
        return self.ffi_value.cupsWidth
