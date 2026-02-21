from typing import Any, Dict

from cups.enums.http import HttpStatus
from cups.enums.ipp import IPPStatus
from cups.types.cups import cupsDest, cupsDestInfo, cupsOption

from .base import _Base, _cups

_lib = _cups.lib


class DocumentMixin(_Base):
    http: Any

    def startDestDocument(
        self,
        dest: cupsDest,
        dest_info: cupsDestInfo,
        job_id: int,
        docname: str,
        format: str,
        options: Dict[str, cupsOption],
        last_document: bool,
    ) -> HttpStatus:
        status = _lib.cupsStartDestDocument(
            self.http,
            dest.ffi_value,
            dest_info.ffi_value,
            job_id,
            docname.encode(),
            format.encode(),
            len(options),
            cupsOption.to_cffi_list(options),
            last_document,
        )
        return HttpStatus(status)

    def finishDestDocument(self, dest: cupsDest, dinfo: cupsDestInfo) -> IPPStatus:
        return IPPStatus(
            _lib.cupsFinishDestDocument(self.http, dest.ffi_value, dinfo.ffi_value)
        )

    def writeRequestData(self, buffer: str, len: int) -> HttpStatus:
        return HttpStatus(_lib.cupsWriteRequestData(self.http, buffer.encode(), len))
