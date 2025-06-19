from cups.utils import _bytes_to_value
from . import _cups

from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union
)

from cups.types import cupsOption

_ffi = _cups.ffi
_lib = _cups.lib

def addOption(name: str, value: Union[int, str], options: Optional[List[cupsOption]]) -> Dict[str, cupsOption]:
    c_opts: Any
    if options is None:
        c_opts = cupsOption.cffi_new("**")
    elif options is not None:
        c_opts = cupsOption.to_cffi_list(opts=options)
    else:
        raise ValueError("options variable needed to be passed if not creating a new options list")

    c_num_options = _ffi.cast("size_t", len(options) if options else 0)
    c_name = _ffi.new("char[]", name.encode("utf-8"))
    c_value = _ffi.new("char[]", str(value).encode("utf-8"))
    count = _lib.cupsAddOption(
        c_name, c_value, c_num_options, c_opts
    )

    return cupsOption.from_cffi_list(c_opts, count)


def getOption(name: str, options: Dict[str, cupsOption]) -> Optional[cupsOption]:
    return options[name]
