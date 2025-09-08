from cups import _cups
from cups.types import cupsLang
from cups.enums import CUPSEncoding
from cups.utils import _bytes_to_value, _value_to_bytes

_ffi = _cups.ffi
_lib = _cups.lib

def langAddStrings(lang: str, strings: list[str]) -> bool:
    return bool(_lib.cupsLangAddStrings(lang.encode(), _value_to_bytes(strings)))

def langDefault() -> cupsLang:
    return cupsLang(_lib.cupsLangDefault())

def langFind(lang: str) -> cupsLang:
    return cupsLang(_lib.cupsLangFind(lang.encode()))

def langGetEncoding() -> str:
    return CUPSEncoding(_lib.cupsLangGetEncoding())

def langGetString(message: str, lang: cupsLang = None) -> str:
    if not lang:
        lang = langDefault()
    return _bytes_to_value(_lib.cupsLangGetString(lang.ffi_value, message.encode()))
