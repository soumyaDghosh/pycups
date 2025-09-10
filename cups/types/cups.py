from typing import (  # noqa: D100
    Any,
    ClassVar,
    Optional,
    Union,
    cast,
)

from cups.enums.ipp import IPPOp, IPPTag
from cups.types.ipp import IPPAttribute, IPPRequest
from cups.utils import (
    _bytes_to_value,
)

from .base import _ffi, _lib, cupsBaseClass


class cupsDestInfo(cupsBaseClass):  # noqa: N801
    """A class representing a CUPS destination info."""

    ffi_name: ClassVar[str] = "cups_dinfo_t"


class cupsOption(cupsBaseClass):  # noqa: D101, N801
    @property
    def name(self) -> str:  # noqa: D102
        return cast(str, _bytes_to_value(self.ffi_value.name))

    @property
    def value(self) -> Optional[Union[str, bool]]:  # noqa: D102
        return _bytes_to_value(self.ffi_value.value)

    ffi_name = "cups_option_t"

    def to_dict(self) -> dict:  # noqa: D102
        return {"name": self.name, "value": self.value}

    def toAttribute(self, ipp_req: IPPRequest, group_tag: IPPTag) -> IPPAttribute:  # noqa: N802
        """Convert this cupsOption into an IPPAttribute.

        Args:
            ipp_req (IPPRequest): The IPPRequest to add the attribute to.
            group_tag (IPPTag): The group tag to use for the attribute.

        Returns:
            IPPAttribute: The created IPPAttribute.

        """
        return IPPAttribute(
            _lib.cupsEncodeOption(
                ipp_req.ffi_value,
                group_tag,
                self.name.encode(),
                cast(str, self.value).encode() if self.value else b"",
            )
        )

    @classmethod
    def to_cffi_list(cls, opts: "dict[str, cupsOption]") -> Any:  # noqa: ANN401, D102
        count = len(opts)
        c_opts = _ffi.new(f"cups_option_t[{count}]")

        for i, opt in enumerate(opts.values()):
            c_opts[i].name = _ffi.new("char[]", opt.name.encode("utf-8"))
            c_opts[i].value = _ffi.new(
                "char[]",
                str(opt.value).encode("utf-8") if opt.value is not None else b"",
            )

        return c_opts

    @classmethod
    def from_cffi_list(cls, opts: Any, count: int) -> "dict[str, cupsOption]":  # noqa: ANN401, D417
        """Convert a list of CFFI dest structs to a list of python cupsOption.

        Args:
            dests (Any): The CFFI *cups_option_t pointer.

        Returns:
            List[cupsOption]: The list of cupsDest.

        """
        results: dict[str, cupsOption] = {}
        for i in range(count):
            new_opt: Any = opts[i]
            results[str(_bytes_to_value(new_opt.name))] = cupsOption.from_cffi(  # type: ignore[attr-defined]
                opt=new_opt
            )

        return results

    def __str__(self) -> str:
        return f"{self.name}: {self.value})"


class cupsDest(cupsBaseClass):  # noqa: D101, N801
    @property
    def name(self) -> str:  # noqa: D102
        return str(_bytes_to_value(self.ffi_value.name))

    @property
    def instance(self) -> Optional[str]:  # noqa: D102
        return _bytes_to_value(self.ffi_value.instance)  # type: ignore[return-value]

    @property
    def options(self) -> dict[str, cupsOption]:  # noqa: D102
        return cupsOption.from_cffi_list(
            opts=self.ffi_value.options, count=self.ffi_value.num_options
        )

    @property
    def is_default(self) -> bool:  # noqa: D102
        return self.ffi_value.is_default

    ffi_name = "cups_dest_t"
    ffi_free = "cupsFreeDests"

    @classmethod
    def from_cffi_list(cls, dests: "cupsDest", count: int) -> "dict[str, cupsDest]":
        """Convert a list of CFFI dest structs to a list of python cupsDest.

        Args:
            dests (Any): The CFFI *cups_dest_t pointer to a pointer.
            count (int): The number of destinations in the list.

        Returns:
            Dict[str, cupsDest]: The list of cupsDest.

        """
        results: dict[str, cupsDest] = {}
        for i in range(count):
            new_dest: Any = dests.ffi_value[0][i]
            results[str(_bytes_to_value(new_dest.name))] = cupsDest.from_cffi(
                dest=new_dest
            )

        return results

    @classmethod
    def from_cffi(cls, dest: Any) -> "cupsDest":  # noqa: ANN401
        """Convert a single CFFI dest struct to a Python cupsDest object.

        Args:
            dest (Any): The CFFI cups_dest_t struct.

        Returns:
            cupsDest: The equivalent Python object.

        """
        return cls(dest)

    @classmethod
    def to_cffi_list(cls, dests: "dict[str, cupsDest]") -> Any:  # noqa: ANN401, D102
        count = len(dests)
        c_dests = _ffi.new(f"cups_dest_t[{count}]")

        for i, dest in enumerate(dests.values()):
            c_dests[i].name = _ffi.new("char[]", dest.name.encode("utf-8"))
            c_dests[i].instance = _ffi.new(
                "char[]",
                dest.instance.encode("utf-8") if dest.instance is not None else b"",
            )
            c_dests[i].is_default = dest.is_default
            c_dests[i].num_options = len(dest.options)
            c_dests[i].options = cupsOption.to_cffi_list(dest.options)

        if cls._is_valid_c_list(c_dests):
            return c_dests
        return None

    def getPrinterAttributes(self, http: Any) -> dict[str, IPPAttribute]:  # noqa: ANN401, D102, N802
        ctype = _ffi.typeof(http)
        if ctype.kind != "pointer" and ctype.cname != "struct _http_s *":
            raise TypeError("http must be of type struct _http_s *")  # noqa: TRY003

        req: IPPRequest = IPPRequest(IPPOp.GET_PRINTER_ATTRIBUTES)
        req.addString(
            group=IPPTag.OPERATION,
            value_tag=IPPTag.URI,
            name="printer-uri",
            value=self.options["printer-uri-supported"].value,  # type: ignore[arg-type]
        )
        res: IPPRequest = IPPRequest(_lib.cupsDoRequest(http, req.ffi_value, b"/"))
        if res is not None:
            return {
                attr.name: attr
                for attr in res.attributes
                if isinstance(attr, IPPAttribute)
            }
        return None

    def __str__(self) -> str:
        return f"{self.name} (Default)" if self.is_default else self.name


class cupsJob(cupsBaseClass):  # noqa: D101, N801
    ffi_name: ClassVar[str] = "cups_job_t"
    ffi_free: ClassVar[str] = "cupsFreeJobs"

    @property
    def id(self) -> int:  # noqa: D102
        return self.ffi_value.id

    @property
    def dest(self) -> str:  # noqa: D102
        return str(_bytes_to_value(self.ffi_value.dest))

    @property
    def title(self) -> Optional[str]:  # noqa: D102
        return _bytes_to_value(self.ffi_value.title)  # type: ignore[return-value]

    @property
    def user(self) -> Optional[str]:  # noqa: D102
        return _bytes_to_value(self.ffi_value.user)  # type: ignore[return-value]

    @property
    def format(self) -> Optional[str]:  # noqa: D102
        return _bytes_to_value(self.ffi_value.format)  # type: ignore[return-value]

    @property
    def state(self) -> int:  # noqa: D102
        return self.ffi_value.state

    @property
    def size(self) -> int:  # noqa: D102
        return self.ffi_value.size

    @property
    def priority(self) -> int:  # noqa: D102
        return self.ffi_value.priority

    @property
    def completed_time(self) -> int:  # noqa: D102
        return self.ffi_value.completed_time

    @property
    def creation_time(self) -> int:  # noqa: D102
        return self.ffi_value.creation_time

    @property
    def processing_time(self) -> int:  # noqa: D102
        return self.ffi_value.processing_time

    @classmethod
    def from_cffi(cls, job: Any) -> "cupsJob":  # noqa: ANN401
        """Wrap a single cups_job_t struct in a cupsJob instance."""
        return cls(job)

    @classmethod
    def from_cffi_list(cls, jobs: Any, count: int) -> dict[int, "cupsJob"]:  # noqa: ANN401
        """Convert CFFI array of cups_job_t into a dict keyed by job ID."""
        results: dict[int, cupsJob] = {}
        for i in range(count):
            new_job = jobs[i]
            results[new_job.id] = cls.from_cffi(new_job)
        return results

    def to_cffi(self) -> Any:  # noqa: ANN401
        """Convert this cupsJob instance into a CFFI cups_job_t struct."""
        c_job = _ffi.new(self.ffi_name + " *")
        c_job[0].id = self.id
        c_job[0].dest = _ffi.new("char[]", self.dest.encode("utf-8"))
        c_job[0].title = _ffi.new(
            "char[]", self.title.encode("utf-8") if self.title else b""
        )
        c_job[0].user = _ffi.new(
            "char[]", self.user.encode("utf-8") if self.user else b""
        )
        c_job[0].format = _ffi.new(
            "char[]", self.format.encode("utf-8") if self.format else b""
        )
        c_job[0].state = self.state
        c_job[0].size = self.size
        c_job[0].priority = self.priority
        c_job[0].completed_time = self.completed_time
        c_job[0].creation_time = self.creation_time
        c_job[0].processing_time = self.processing_time
        return c_job


class cupsLang(cupsBaseClass):  # noqa: D101, N801
    ffi_name = "cups_lang_t"

    def __str__(self) -> str:
        return _bytes_to_value(_lib.cupsLangGetName(self.ffi_value))  # type: ignore[return-value]
