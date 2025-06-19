from . import _cups

from .utils import _bytes_to_value

_ffi = _cups.ffi
_lib = _cups.lib

def areCredsValidForName(common_name: str, credentials: str):
    c_common_name = _ffi.new("char[]", common_name)
    c_credentials = _ffi.new("char[]", credentials)

    is_valid = _bytes_to_value(_lib.cupsAreCredentialsValidForName(
        c_common_name, c_credentials
    ))

    if isinstance(is_valid, bool):
        return is_valid

    return False
