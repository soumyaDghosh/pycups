from enum import IntFlag

from cups import _cups

_lib = _cups.lib


class WhichJobs(IntFlag):
    ACTIVE = _lib.CUPS_WHICHJOBS_ACTIVE
    ALL = _lib.CUPS_WHICHJOBS_ALL
    COMPLETED = _lib.CUPS_WHICHJOBS_COMPLETED
