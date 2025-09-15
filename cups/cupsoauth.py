from cups.types import cupsJWT
import json
from cups._cups import _lib
from cups.utils import _bytes_to_value, _value_to_bytes
from cups.enums import CUPSOGrant

def oAuthClearTokens(auth_uri: str, resource_uri: str) -> None:
    _lib.cupsOAuthClearTokens(auth_uri.encode(), resource_uri.encode())


def oAuthCopyAccessToken(auth_uri: str, resource_uri: str, time: int) -> str:
    return _bytes_to_value(
        _lib.cupsOAuthCopyAccessToken(
            auth_uri.encode(),
            resource_uri.encode(),
            time,
        )
    )


def oAuthCopyClientId(auth_uri: str, redirect_uri: str) -> str:
    return _bytes_to_value(
        _lib.cupsOAuthCopyClientId(
            auth_uri.encode(),
            redirect_uri.encode(),
        )
    )


def oAuthCopyRefreshToken(auth_uri: str, resource_uri: str) -> str:
    return _bytes_to_value(
        _lib.cupsOAuthCopyRefreshToken(
            auth_uri.encode(),
            resource_uri.encode(),
        )
    )


def oAuthCopyUserId(auth_uri: str, resource_uri: str) -> cupsJWT:
    return cupsJWT(
        _lib.cupsOAuthCopyUserId(
            auth_uri.encode(),
            resource_uri.encode(),
        )
    )


def oAuthGetAuthorizationCode(
    auth_uri: str, metadata: dict, resource_uri: str, scopes: list[str], redirect_uri: str
) -> str:
    return _bytes_to_value(
        _lib.cupsOAuthGetAuthorizationCode(
            auth_uri.encode(),
            _value_to_bytes(metadata),
            resource_uri.encode(),
            _bytes_to_value(scopes),
            redirect_uri.encode()
        )
    )


def oAuthGetClientId(auth_uri: str, metadata: dict, redirect_uri: str, logo_uri: str, tos_uri: str) -> str:
    return _bytes_to_value(
        _lib.cupsOAuthGetClientId(
            auth_uri.encode(),
            _value_to_bytes(metadata),
            redirect_uri.encode(),
            logo_uri.encode(),
            tos_uri.encode()
        )
    )


def oAuthGetMetadata(auth_uri: str) -> dict:
    json_value = _bytes_to_value(_lib.cupsOAuthGetMetadata(auth_uri.encode()))
    return json.loads(json_value) if json_value else {}


def oAuthGetTokens(auth_uri: str, metadata: dict, resource_uri: str, grant_code: str, grant_type: CUPSOGrant, redirect_uri: str, access_expires: int) -> str:
    return _bytes_to_value(
        _lib.cupsOAuthGetTokens(
            auth_uri.encode(),
            _value_to_bytes(metadata),
            resource_uri.encode(),
            grant_code.encode(),
            grant_type.value,
            redirect_uri.encode(),
            access_expires
        )
    )

def oAuthMakeAuthorizationURL(
    auth_uri: str,
    metadata: dict,
    resource_uri: str,
    scopes: list[str],
    client_id: str,
    code_verifier: str,
    nonce: str,
    redirect_uri: str,
    state: str,
) -> str:
    return _bytes_to_value(
        _lib.cupsOAuthMakeAuthorizationURL(
            auth_uri.encode(),
            _value_to_bytes(metadata),
            resource_uri.encode(),
            _value_to_bytes(scopes),
            client_id.encode(),
            code_verifier.encode(),
            nonce.encode(),
            redirect_uri.encode(),
            state.encode(),
        )
)


def oAuthSaveClientData(
    auth_uriL: str,
    redirect_uri: str,
    client_id: str,
    client_secret: str,
) -> None:
    _lib.cupsOAuthSaveClientData(
        auth_uriL.encode(),
        redirect_uri.encode(),
        client_id.encode(),
        client_secret.encode(),
    )


def oAuthSaveTokens(auth_uri: str, resource_uri: str, access_token: str, access_expires: int, user_id: str, refresh_token: str) -> None:
    _lib.cupsOAuthSaveTokens(
        auth_uri.encode(),
        resource_uri.encode(),
        access_token.encode(),
        access_expires,
        user_id.encode(),
        refresh_token.encode(),
    )
