from cups.types.base import cupsBaseClass, _lib
from cups.utils import _bytes_to_value

class cupsLang(cupsBaseClass):
    ffi_name = "cups_lang_t"

    def __str__(self):
        return _bytes_to_value(_lib.cupsLangGetName(self.ffi_value))
