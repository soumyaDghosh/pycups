from typing import (
    Any,
    ClassVar,
    Dict,
    Optional,
)

from cups.utils import (
    _bytes_to_value,
)

from cups.types.ipp import IPPAttribute, IPPRequest
from cups.enums.ipp import IPPOp, IPPTag

from .base import cupsBaseClass, _ffi, _lib


class cupsDestInfo(cupsBaseClass):
    """A class representing a CUPS destination info"""

    ffi_name: ClassVar[str] = "cups_dinfo_t"

    def __str__(self):
        return super().__str__()


class cupsOption(cupsBaseClass):
    @property
    def name(self) -> str:
        return _bytes_to_value(self.ffi_value.name)

    @property
    def value(self) -> Optional[Any]:
        return _bytes_to_value(self.ffi_value.value)

    ffi_name = "cups_option_t"

    def to_dict(self) -> dict:
        return {"name": self.name, "value": self.value}

    @classmethod
    def from_cffi(cls, opt: Any) -> "cupsOption":
        """
        Convert a single CFFI dest struct to a Python cupsOption object.

        Args:
            dest (Any): The CFFI cups_option_t struct.

        Returns:
            cupsOption: The equivalent Python object.
        """
        return cls(opt)

    @classmethod
    def to_cffi_list(cls, opts: "Dict[str, cupsOption]") -> Any:
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
    def from_cffi_list(cls, opts: Any, count: int) -> "Dict[str, cupsOption]":
        """
        Convert a list of CFFI dest structs to a list of python cupsOption.

        Args:
            dests (Any): The CFFI *cups_option_t pointer.

        Returns:
            List[cupsOption]: The list of cupsDest.
        """
        results: Dict[str, cupsOption] = {}
        for i in range(count):
            new_opt: Any = opts[i]
            results[str(_bytes_to_value(new_opt.name))] = cupsOption.from_cffi(
                opt=new_opt
            )

        return results

    def __str__(self):
        return f"{self.name}: {self.value})"


class cupsDest(cupsBaseClass):
    @property
    def name(self) -> str:
        return str(_bytes_to_value(self.ffi_value.name))

    @property
    def instance(self) -> Optional[str]:
        return _bytes_to_value(self.ffi_value.instance)

    @property
    def options(self) -> Dict[str, cupsOption]:
        return cupsOption.from_cffi_list(
            opts=self.ffi_value.options, count=self.ffi_value.num_options
        )

    @property
    def is_default(self) -> bool:
        return self.ffi_value.is_default

    ffi_name = "cups_dest_t"
    ffi_free = "cupsFreeDests"

    @classmethod
    def from_cffi_list(cls, dests: "cupsDest", count: int) -> "Dict[str, cupsDest]":
        """
        Convert a list of CFFI dest structs to a list of python cupsDest.

        Args:
            dests (Any): The CFFI *cups_dest_t pointer to a pointer.
            count (int): The number of destinations in the list.

        Returns:
            Dict[str, cupsDest]: The list of cupsDest.
        """
        results: Dict[str, cupsDest] = {}
        for i in range(count):
            new_dest: Any = dests.ffi_value[0][i]
            results[str(_bytes_to_value(new_dest.name))] = cupsDest.from_cffi(
                dest=new_dest
            )

        return results

    @classmethod
    def from_cffi(cls, dest: Any) -> "cupsDest":
        """
        Convert a single CFFI dest struct to a Python cupsDest object.

        Args:
            dest (Any): The CFFI cups_dest_t struct.

        Returns:
            cupsDest: The equivalent Python object.
        """
        return cls(dest)

    @classmethod
    def to_cffi_list(cls, dests: "Dict[str, cupsDest]") -> Any:
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

        return c_dests

    def getPrinterAttributes(self, http: Any) -> dict[str, IPPAttribute]:
        ctype = _ffi.typeof(http)
        if ctype.kind != "pointer" and ctype.cname != "struct _http_s *":
            raise TypeError("http must be of type struct _http_s *")

        req: IPPRequest = IPPRequest(IPPOp.GET_PRINTER_ATTRIBUTES)
        req.addString(
            group=IPPTag.OPERATION,
            value_tag=IPPTag.URI,
            name="printer-uri",
            value=self.options["printer-uri-supported"].value,
        )
        res: IPPRequest = IPPRequest(_lib.cupsDoRequest(http, req.ffi_value, b"/"))
        if res is not None:
            return {
                attr.name: attr
                for attr in res.attributes
                if isinstance(attr, IPPAttribute)
            }

    def __str__(self):
        return f"{self.name} (Default)" if self.is_default else self.name


class cupsJob(cupsBaseClass):
    ffi_name: ClassVar[str] = "cups_job_t"
    ffi_free: ClassVar[str] = "cupsFreeJobs"

    @property
    def id(self) -> int:
        return self.ffi_value.id

    @property
    def dest(self) -> str:
        return str(_bytes_to_value(self.ffi_value.dest))

    @property
    def title(self) -> Optional[str]:
        return _bytes_to_value(self.ffi_value.title)

    @property
    def user(self) -> Optional[str]:
        return _bytes_to_value(self.ffi_value.user)

    @property
    def format(self) -> Optional[str]:
        return _bytes_to_value(self.ffi_value.format)

    @property
    def state(self) -> int:
        return self.ffi_value.state

    @property
    def size(self) -> int:
        return self.ffi_value.size

    @property
    def priority(self) -> int:
        return self.ffi_value.priority

    @property
    def completed_time(self) -> int:
        return self.ffi_value.completed_time

    @property
    def creation_time(self) -> int:
        return self.ffi_value.creation_time

    @property
    def processing_time(self) -> int:
        return self.ffi_value.processing_time

    @classmethod
    def from_cffi(cls, job: Any) -> "cupsJob":
        """Wrap a single cups_job_t struct in a cupsJob instance."""
        return cls(job)

    @classmethod
    def from_cffi_list(cls, jobs: Any, count: int) -> Dict[int, "cupsJob"]:
        """Convert CFFI array of cups_job_t into a dict keyed by job ID."""
        results: Dict[int, cupsJob] = {}
        for i in range(count):
            new_job = jobs[i]
            results[new_job.id] = cls.from_cffi(new_job)
        return results

    def to_cffi(self) -> Any:
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

    def __str__(self):
        return super.__str__()
