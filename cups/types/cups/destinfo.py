from cups.types.base import cupsBaseClass, _ffi, _lib

class cupsDestInfo(cupsBaseClass):
    """A class representing a CUPS destination info"""

    ffi_name: str = "cups_dinfo_t"
