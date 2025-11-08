from typing import Any, Optional

from cups import _cups
from cups.enums.ipp import IPPOp, IPPState, IPPTag
from cups.types.ipp import IPPError, IPPRequest, IPPStatus

from .base import _Base

_lib = _cups.lib


class IPPMixin(_Base):
    http: Any

    def addPrinter(
        self,
        name: str,
        info: Optional[str] = None,
        location: Optional[str] = None,
        device: Optional[str] = None,
    ) -> None:
        req: IPPRequest = self._add_or_modify_printer(name)

        if info:
            req.addString(
                group=IPPTag.PRINTER,
                value_tag=IPPTag.TEXT,
                name="printer-info",
                value=info,
            )

        if location:
            req.addString(
                group=IPPTag.PRINTER,
                value_tag=IPPTag.TEXT,
                name="printer-location",
                value=location,
            )

        if device:
            req.addString(
                group=IPPTag.PRINTER,
                value_tag=IPPTag.URI,
                name="device-uri",
                value=device,
            )

        answer: IPPRequest = IPPRequest(
            _lib.cupsDoRequest(self.http, req.ffi_value, b"/admin/")
        )

        if not answer or answer.statuscode > IPPStatus.OK_CONFLICTING:
            raise IPPError(answer)

    def addPrinterToClass(self, name: str, class_name: str) -> None:
        req: IPPRequest = IPPRequest(IPPOp.GET_PRINTER_ATTRIBUTES)
        class_uri = f"ipp://localhost/classes/{class_name}"
        req.addString(
            group=IPPTag.OPERATION,
            value_tag=IPPTag.URI,
            name="printer-uri",
            value=class_uri,
        )

        answer: IPPRequest = IPPRequest(
            _lib.cupsDoRequest(self.http, req.ffi_value, b"/")
        )

        if answer:
            member_names = next(
                (attr for attr in answer.attributes if attr.name == "member-names"),
                None,
            )
            if member_names and name in member_names.values:
                raise RuntimeError(
                    f"Printer '{name}' is already a member of class '{class_name}'"
                )

        req: IPPRequest = IPPRequest(IPPOp.CUPS_ADD_MODIFY_CLASS)
        req.addString(
            group=IPPTag.OPERATION,
            value_tag=IPPTag.URI,
            name="printer-uri",
            value=class_uri,
        )
        printer_uri = f"ipp://localhost/printers/{name}"

        member_uris = None
        if answer:
            member_uris = next(
                (attr for attr in answer.attributes if attr.name == "member-uris"),
                None,
            )

        if member_uris:
            old_values = list(member_uris.values)
            old_values.append(printer_uri)
            req.addStrings(
                group=IPPTag.PRINTER,
                value_tag=IPPTag.URI,
                name="member-uris",
                values=old_values,
            )
        else:
            req.addString(
                group=IPPTag.PRINTER,
                value_tag=IPPTag.URI,
                name="member-uris",
                value=printer_uri,
            )

        answer: IPPRequest = IPPRequest(
            _lib.cupsDoRequest(self.http, req.ffi_value, b"/admin/")
        )

        if not answer or answer.statuscode > IPPStatus.OK_CONFLICTING:
            raise RuntimeError(
                f"IPP error: {answer.statuscode if answer else 'no answer'}"
            )

    def getResponse(self, resource: str) -> IPPRequest:
        return IPPRequest(_lib.cupsGetResponse(self.http, resource.encode()))

    def ippRead(self, ipp: IPPRequest) -> IPPState: ...
