from typing import Any
from cups import _cups
from cups.types.ipp import IPPRequest, IPPStatus, IPPError
from cups.enums.ipp import IPPOp, IPPTag


class _Base:
    http: Any

    def _add_or_modify_printer(self, name: str) -> None:
        uri: str = f"ipp://localhost/printers/{name}"
        req: IPPRequest = IPPRequest(IPPOp.CUPS_ADD_MODIFY_PRINTER)
        req.addString(
            group=IPPTag.OPERATION, value_tag=IPPTag.URI, name="printer-uri", value=uri
        )

        return req
