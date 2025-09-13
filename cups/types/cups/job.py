from cups.types.base import cupsBaseClass, _ffi, _lib
from cups.utils import _bytes_to_value
from typing import Any, Dict, Optional

class cupsJob(cupsBaseClass):
    ffi_name: str = "cups_job_t"
    ffi_free: str = "cupsFreeJobs"

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
