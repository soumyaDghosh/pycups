from enum import IntFlag  # noqa: D100

from cups import _cups

_lib = _cups.lib


class WhichJobs(IntFlag):  # noqa: D101
    ACTIVE = _lib.CUPS_WHICHJOBS_ACTIVE
    ALL = _lib.CUPS_WHICHJOBS_ALL
    COMPLETED = _lib.CUPS_WHICHJOBS_COMPLETED
