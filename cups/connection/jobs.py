from typing import Any, Optional

from cups import _cups
from cups.enums.ipp import IPPOp, IPPStatus, IPPTag
from cups.types.ipp import IPPError, IPPRequest

_lib = _cups.lib


class JobMixin:
    http: Any

    def _do_printer_request(
        self, name: str, op: IPPOp, reason: Optional[str] = None
    ) -> None:
        uri: str = f"ipp://localhost/printers/{name}"
        req: IPPRequest = IPPRequest.cffi_new(op)
        req.addString(
            group=IPPTag.OPERATION, value_tag=IPPTag.URI, name="printer-uri", value=uri
        )

        if reason is not None:
            req.addString(
                group=IPPTag.OPERATION,
                value_tag=IPPTag.TEXT,
                name="printer-state-message",
                value=reason,
            )

        answer: IPPRequest = IPPRequest(
            _lib.cupsDoRequest(self.http, req.ffi_value, "/admin/")
        )

        if not answer or answer.statuscode > IPPStatus.OK_CONFLICTING:
            raise IPPError(answer)

    def acceptJobs(self, queue_name: str) -> None:
        return self._do_printer_request(queue_name, op=IPPOp.CUPS_ACCEPT_JOBS)

    def rejectJobs(self, queue_name: str) -> None:
        return self._do_printer_request(queue_name, op=IPPOp.CUPS_REJECT_JOBS)
