from cups import _cups
from cups.enums.http import HttpEncryption
from cups.types.cups import cupsDest
from cups.types.ipp import IPPStatus
from cups.utils import _bytes_to_value, _value_to_bytes
from typing import Dict, Optional, Tuple
from pathlib import Path

_ffi = _cups.ffi
_lib = _cups.lib


def areCredentialsValidForName(common_name: str, credentials: str) -> bool:
    ok = _lib.cupsAreCredentialsValidForName(common_name.encode(), credentials.encode())
    return bool(_bytes_to_value(ok))


def copyCredentialsKey(
    path: Path,
    common_name: str,
    *,
    is_key: bool = False,
    is_public_key: bool = False,
    copy_req: bool = False,
) -> str:
    if (is_key and copy_req) or (is_public_key and copy_req):
        raise ValueError(
            "Cannot copy the key and the credentials request at the same time"
        )

    if copy_req:
        return _bytes_to_value(
            _lib.cupsCopyCredentialsRequest(str(path).encode(), common_name.encode())
        )

    if is_public_key:
        return _bytes_to_value(
            _lib.cupsCopyCredentialsPublicKey(str(path).encode(), common_name.encode())
        )

    if is_key:
        return _bytes_to_value(
            _lib.cupsCopyCredentialsKey(str(path).encode(), common_name.encode())
        )

    return _bytes_to_value(
        _lib.cupsCopyCredentials(str(path).encode(), common_name.encode())
    )


def copyDest(dest: cupsDest, dests: Dict[str, cupsDest]) -> Dict[str, cupsDest]:
    """
    Returns a new list of dests
    """
    num_dests = _lib.cupsCopyDest(
        dest.ffi_value, len(dests), cupsDest.to_cffi_list(dests)
    )
    return cupsDest.from_cffi_list(dests=dests, count=num_dests)


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


def getUserAgent() -> str:
    return _bytes_to_value(_lib.cupsGetUserAgent())


def setUserAgent(user_agent: str):
    c_user_agent = _value_to_bytes(user_agent)
    _lib.cupsSetUserAgent(c_user_agent)


def getDestWithURI(uri: str, name: Optional[str] = None) -> cupsDest:
    c_uri = _ffi.new("char[]", uri.encode("utf-8"))
    c_name = _ffi.new("char[]", name.encode("utf-8")) if name else _ffi.NULL
    dest = _lib.cupsGetDestWithURI(c_name, c_uri)
    if dest == _ffi.NULL:
        raise RuntimeError("No such destination found")
    return cupsDest(ffi_value=dest)


def getError() -> Tuple[IPPStatus, Optional[str]]:
    status: IPPStatus = IPPStatus(_lib.cupsGetError())
    message: str = _bytes_to_value(_lib.cupsGetErrorString())

    return (status, message)
