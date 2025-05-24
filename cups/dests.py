from .internal import libcups_binding
from cffi import FFI
from typing import List
from .types import (
    cupsDest,
    cupsOption
)

ffi: FFI = libcups_binding.ffi
lib = libcups_binding.lib

def getDests() -> List[cupsDest]:
    dests = ffi.new("cups_dest_t **")
    count = lib.cupsGetDests(ffi.NULL, dests)
    results = []
    for i in range(count):
        dest = dests[0][i]
        dest_name = ffi.string(dest.name).decode("utf-8")
        dest_instance = ffi.string(dest.instance).decode("utf-8") if dest.instance != ffi.NULL else None
        is_default = bool(dest.is_default)
        opts = []
        for j in range(dest.num_options):
            opt = dest.options[j]
            opt_name = ffi.string(opt.name).decode()
            opt_value = ffi.string(opt.value).decode()
            opts.append(cupsOption(opt_name, opt_value))
        results.append(cupsDest(dest_name, dest_instance, is_default, opts))
    lib.cupsFreeDests(count, dests[0])
    return results
