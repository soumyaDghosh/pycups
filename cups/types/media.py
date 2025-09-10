from cups.utils import _bytes_to_value  # noqa: D100

from .base import cupsBaseClass


class cupsMedia(cupsBaseClass):  # noqa: D101, N801
    ffi_name = "cups_media_t"

    @property
    def width(self) -> int:  # noqa: D102
        return self.ffi_value.width

    @property
    def length(self) -> int:  # noqa: D102
        return self.ffi_value.length

    @property
    def bottom(self) -> int:  # noqa: D102
        return self.ffi_value.bottom_margin

    @property
    def left(self) -> int:  # noqa: D102
        return self.ffi_value.left_margin

    @property
    def right(self) -> int:  # noqa: D102
        return self.ffi_value.right_margin

    @property
    def top(self) -> int:  # noqa: D102
        return self.ffi_value.top_margin

    @property
    def media(self) -> str:  # noqa: D102
        return _bytes_to_value(self.ffi_value.media)

    @property
    def color(self) -> int:  # noqa: D102
        return _bytes_to_value(self.ffi_value.color)

    @property
    def source(self) -> str:  # noqa: D102
        return _bytes_to_value(self.ffi_value.source)

    @property
    def type(self) -> str:  # noqa: D102
        return _bytes_to_value(self.ffi_value.type)
