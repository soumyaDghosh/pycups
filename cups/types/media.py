from cups.utils import _bytes_to_value

from .base import cupsBaseClass


class cupsMedia(cupsBaseClass):
    ffi_name = "cups_media_t"

    @property
    def width(self) -> int:
        return self.ffi_value.width

    @property
    def length(self) -> int:
        return self.ffi_value.length

    @property
    def bottom(self) -> int:
        return self.ffi_value.bottom_margin

    @property
    def left(self) -> int:
        return self.ffi_value.left_margin

    @property
    def right(self) -> int:
        return self.ffi_value.right_margin

    @property
    def top(self) -> int:
        return self.ffi_value.top_margin

    @property
    def media(self) -> str:
        return _bytes_to_value(self.ffi_value.media)

    @property
    def color(self) -> int:
        return _bytes_to_value(self.ffi_value.color)

    @property
    def source(self) -> str:
        return _bytes_to_value(self.ffi_value.source)

    @property
    def type(self) -> str:
        return _bytes_to_value(self.ffi_value.type)
