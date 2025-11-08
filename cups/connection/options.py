from typing import Any

from cups import _cups
from cups.enums.ipp import IPPTag
from cups.types.ipp import IPPError, IPPRequest, IPPStatus

from .base import _Base

_ffi = _cups.ffi
_lib = _cups.lib


class OptionsMixin(_Base):
    http: Any

    def addPrinterOptionDefault(
        self, name: str, option: str, value: str | list
    ) -> None:
        req: IPPRequest = self._add_or_modify_printer(name)

        if isinstance(value, list):
            req.addStrings(
                group=IPPTag.PRINTER,
                value_tag=IPPTag.NAME,
                name=name,
                values=value,
            )
        elif isinstance(value, str):
            req.addString(
                group=IPPTag.PRINTER,
                value_tag=IPPTag.NAME,
                name=name,
                value=value,
            )

        answer: IPPRequest = IPPRequest(
            _lib.cupsDoRequest(self.http, req.ffi_value, "/admin/")
        )

        if not answer:
            raise IPPError("No response from server")

        if answer.statuscode == IPPStatus.ERROR_NOT_POSSIBLE:
            raise IPPError("Operation not possible, the printer may be a class")
