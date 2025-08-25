from cups import _cups
from typing import Any, Optional

_ffi = _cups.ffi


def _strtobool(val: str) -> Optional[bool]:
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif val in ("n", "no", "f", "false", "off", "0"):
        return False
    else:
        return None


def _bytes_to_value(b: bytes) -> Optional[Any]:
    if b == _ffi.NULL:
        return None
    string: str = _ffi.string(b).decode()
    string_to_bool: Optional[bool] = _strtobool(string)
    if isinstance(string_to_bool, bool):
        return string_to_bool
    if string and string.split(",")[0] != "none":
        return string
    return None


def _value_to_bytes(value: Any) -> Any:
    if value is None:
        return _ffi.NULL
    if isinstance(value, list):
        return _ffi.new("char *[]", [_ffi.new("char[]", s.encode()) for s in value])
    if isinstance(value, str):
        return _ffi.new("char[]", value.encode())
