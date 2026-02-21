from enum import IntFlag

from cups import _cups

_lib = _cups.lib


class CUPSMediaFlags(IntFlag):
    BORDERLESS = _lib.CUPS_MEDIA_FLAGS_BORDERLESS
    DEFAULT = _lib.CUPS_MEDIA_FLAGS_DEFAULT
    DUPLEX = _lib.CUPS_MEDIA_FLAGS_DUPLEX
    EXACT = _lib.CUPS_MEDIA_FLAGS_EXACT
    READY = _lib.CUPS_MEDIA_FLAGS_READY
