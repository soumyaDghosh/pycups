from cups import _cups
from cups.enums.http import HttpEncryption
from cups.types.cups import cupsDest
from cups.utils import _bytes_to_value

_ffi = _cups.ffi
_lib = _cups.lib


def getEncryption() -> HttpEncryption:
    encryption = _lib.cupsGetEncryption()
    return HttpEncryption(encryption)


def setEncryption(encryption: HttpEncryption):
    c_encryption = _ffi.cast("http_encryption_t", encryption.value)
    _lib.cupsSetEncryption(c_encryption)


def getPort() -> int:
    return _lib.ippGetPort()


def setPort(port: int):
    _lib.ippSetPort(port)


def getServer() -> str:
    return _bytes_to_value(_lib.cupsGetServer())


def setServer(server: str):
    c_server = _ffi.new("char []", server)
    _lib.cupsSetServer(c_server)


def getUser() -> str:
    return _bytes_to_value(_lib.cupsGetUser())


def setUser(user: str):
    c_user = _ffi.new("char []", user)
    _lib.cupsSetUser(c_user)


def setDefaultDest(name: str, instance: str, num_dests: int, dest: cupsDest):
    c_name = _ffi.new("char[]", name.encode("utf-8")) if name else _ffi.NULL
    c_instance = _ffi.new("char[]", instance.encode("utf-8")) if instance else _ffi.NULL
    _lib.cupsSetDefaultDest(c_name, c_instance, num_dests, dest.ffi_value)
