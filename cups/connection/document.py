from typing import Any  # noqa: D100

from cups.enums.http import HttpStatus
from cups.enums.ipp import IPPStatus
from cups.types.cups import cupsDest, cupsDestInfo, cupsOption

from .base import _Base, _cups

_lib = _cups.lib


class DocumentMixin(_Base):  # noqa: D101
    http: Any

    def startDestDocument(  # noqa: D102, N802, PLR0913
        self,
        dest: cupsDest,
        dest_info: cupsDestInfo,
        job_id: int,
        docname: str,
        format: str,  # noqa: A002
        options: dict[str, cupsOption],
        last_document: bool,  # noqa: FBT001
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

    def finishDestDocument(self, dest: cupsDest, dinfo: cupsDestInfo) -> IPPStatus:  # noqa: D102, N802
        return IPPStatus(
            _lib.cupsFinishDestDocument(self.http, dest.ffi_value, dinfo.ffi_value)
        )

    def writeRequestData(self, buffer: str, len: int) -> HttpStatus:  # noqa: A002, D102, N802
        return HttpStatus(_lib.cupsWriteRequestData(self.http, buffer.encode(), len))
