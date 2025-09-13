from cups.types.base import cupsBaseClass, _lib
from cups.enums import CUPSJWA, CUPSJType
from cups.utils import _bytes_to_value, _value_to_bytes
import json
from typing import Any
from pathlib import Path

class cupsJWT(cupsBaseClass):
    ffi_name = "cups_jwt_t"

    def __init__(self, arg=None):
        if arg and self._is_valid_ctype(arg):
            self.ffi_value = arg

        elif not arg:
            self.ffi_value = _lib.cupsJWTNew()

        else:
            raise ValueError("Invalid arguments passed")

    @property
    def algorithm(self) -> CUPSJWA:
        return CUPSJWA(_lib.cupsJWTGetAlgorithm(self.ffi_value))

    def getClaimNumber(self, claim: str) -> float:
        return _lib.cupsJWTGetClaimNumber(self.ffi_value, claim.encode())

    def getClaimString(self, claim: str) -> str:
        return _bytes_to_value(
            _lib.cupsJWTGetClaimString(self.ffi_value, claim.encode())
        )

    def getClaimType(self, claim: str) -> CUPSJType:
        return CUPSJType(_lib.cupsJWTGetClaimType(self.ffi_value, claim.encode()))

    def getClaimValue(self, claim: str) -> json:
        json_value = _lib.cupsJWTGetClaimValue(self.ffi_value, claim.encode())
        return json.loads(_bytes_to_value(json_value))

    def getClaims(self) -> json:
        json_value = _lib.cupsJWTGetClaims(self.ffi_value)
        return json.loads(_bytes_to_value(json_value))

    def getHeaderNumber(self, header: str) -> float:
        return _lib.cupsJWTGetHeaderNumber(self.ffi_value, header.encode())

    def getHeaderString(self, header: str) -> str:
        return _bytes_to_value(
            _lib.cupsJWTGetHeaderString(self.ffi_value, header.encode())
        )

    def getHeaderType(self, header: str) -> CUPSJType:
        return CUPSJType(_lib.cupsJWTGetHeaderType(self.ffi_value, header.encode()))

    def getHeaderValue(self, header: str) -> json:
        json_value = _lib.cupsJWTGetHeaderValue(self.ffi_value, header.encode())
        return json.loads(_bytes_to_value(json_value))

    def getHeaders(self) -> dict[str, Any]:
        json_value = _lib.cupsJWTGetHeaders(self.ffi_value)
        return json.loads(_bytes_to_value(json_value))

    def hasValidSignature(self, jwk: dict) -> bool:
        return bool(_lib.cupsJWTHasValidSignature(self.ffi_value, _value_to_bytes(jwk)))

    def loadCredentials(self, path: Path, common_name: str) -> dict:
        json_value = _lib.cupsJWTLoadCredentials(
            self.ffi_value, str(path).encode(), common_name.encode()
        )
        return json.loads(_bytes_to_value(json_value))

    def setClaimNumber(self, claim: str, value: float) -> None:
        _lib.cupsJWTSetClaimNumber(self.ffi_value, claim.encode(), value)

    def setClaimString(self, claim: str, value: str) -> None:
        _lib.cupsJWTSetClaimString(self.ffi_value, claim.encode(), value.encode())

    def setHeaderNumber(self, header: str, value: float) -> None:
        _lib.cupsJWTSetHeaderNumber(self.ffi_value, header.encode(), value)

    def setHeaderString(self, header: str, value: str) -> None:
        _lib.cupsJWTSetHeaderString(self.ffi_value, header.encode(), value.encode())

    def sign(self, algorithm: CUPSJWA, jwk: dict) -> bool:
        return bool(_lib.cupsJWTSign(self.ffi_value, algorithm, _value_to_bytes(jwk)))
