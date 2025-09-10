from pathlib import Path  # noqa: D100
from typing import Optional, Union

from cups import _cups
from cups.enums.http import HttpEncryption
from cups.types.cups import cupsDest
from cups.types.ipp import IPPStatus
from cups.utils import _bytes_to_value, _value_to_bytes

_ffi = _cups.ffi
_lib = _cups.lib


def areCredentialsValidForName(common_name: str, credentials: str) -> bool:  # noqa: D103, N802
    ok = _lib.cupsAreCredentialsValidForName(common_name.encode(), credentials.encode())
    return bool(_bytes_to_value(ok))


def copyCredentialsKey(  # noqa: D103, N802
    path: Path,
    common_name: str,
    *,
    is_key: bool = False,
    is_public_key: bool = False,
    copy_req: bool = False,
) -> str | bool | None:
    if (is_key and copy_req) or (is_public_key and copy_req):
        raise ValueError(  # noqa: TRY003
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


def copyDest(dest: cupsDest, dests: dict[str, cupsDest]) -> dict[str, cupsDest]:  # noqa: N802
    """Returns a new list of dests."""  # noqa: D401
    num_dests = _lib.cupsCopyDest(
        dest.ffi_value, len(dests), cupsDest.to_cffi_list(dests)
    )
    return cupsDest.from_cffi_list(dests=dests, count=num_dests)  # type: ignore[arg-type]


def getEncryption() -> HttpEncryption:  # noqa: D103, N802
    encryption = _lib.cupsGetEncryption()
    return HttpEncryption(encryption)


def setEncryption(encryption: HttpEncryption) -> None:  # noqa: D103, N802
    c_encryption = _ffi.cast("http_encryption_t", encryption.value)
    _lib.cupsSetEncryption(c_encryption)


def getPort() -> int:  # noqa: D103, N802
    return _lib.ippGetPort()


def setPort(port: int) -> None:  # noqa: D103, N802
    _lib.ippSetPort(port)


def getServer() -> Optional[Union[str, bool]]:  # noqa: D103, N802
    return _bytes_to_value(_lib.cupsGetServer())


def setServer(server: str) -> None:  # noqa: D103, N802
    c_server = _ffi.new("char []", server)
    _lib.cupsSetServer(c_server)


def getUser() -> Optional[Union[str, bool]]:  # noqa: D103, N802
    return _bytes_to_value(_lib.cupsGetUser())


def setUser(user: str) -> None:  # noqa: D103, N802
    c_user = _ffi.new("char []", user)
    _lib.cupsSetUser(c_user)


def setDefaultDest(name: str, instance: str, num_dests: int, dest: cupsDest) -> None:  # noqa: D103, N802
    c_name = _ffi.new("char[]", name.encode("utf-8")) if name else _ffi.NULL
    c_instance = _ffi.new("char[]", instance.encode("utf-8")) if instance else _ffi.NULL
    _lib.cupsSetDefaultDest(c_name, c_instance, num_dests, dest.ffi_value)


def getUserAgent() -> Optional[Union[str, bool]]:  # noqa: D103, N802
    return _bytes_to_value(_lib.cupsGetUserAgent())


def setUserAgent(user_agent: str) -> None:  # noqa: D103, N802
    c_user_agent = _value_to_bytes(user_agent)
    _lib.cupsSetUserAgent(c_user_agent)


def getDestWithURI(uri: str, name: Optional[str] = None) -> cupsDest:  # noqa: D103, N802
    c_uri = _ffi.new("char[]", uri.encode("utf-8"))
    c_name = _ffi.new("char[]", name.encode("utf-8")) if name else _ffi.NULL
    dest = _lib.cupsGetDestWithURI(c_name, c_uri)
    if dest == _ffi.NULL:
        raise RuntimeError("No such destination found")  # noqa: TRY003
    return cupsDest(ffi_value=dest)  # type: ignore[call-arg]


def getError() -> tuple[IPPStatus, Optional[str]]:  # noqa: D103, N802
    status: IPPStatus = IPPStatus(_lib.cupsGetError())
    message: str = _bytes_to_value(_lib.cupsGetErrorString())  # type: ignore[assignment]

    return (status, message)
