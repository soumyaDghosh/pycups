from enum import IntFlag
from cups import _cups

_lib = _cups.lib


class HttpEncryption(IntFlag):
    IF_REQUESTED = _lib.HTTP_ENCRYPTION_IF_REQUESTED
    NEVER = _lib.HTTP_ENCRYPTION_NEVER
    REQUIRED = _lib.HTTP_ENCRYPTION_REQUIRED
    ALWAYS = _lib.HTTP_ENCRYPTION_ALWAYS
