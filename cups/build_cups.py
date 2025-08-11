from cffi import FFI
import os
import pkgconfig

LIBRARY = "cups3"
VERSION = "3.0rc4"


def get_include_dirs():
    if not (pkgconfig.installed(LIBRARY, f"<={VERSION}")):
        raise Exception(
            "Cannot find pkg-config file for cups3.\nIs CUPS 3.0 development libraries properly installed?"
        )
    cflags = [c[2:] for c in (pkgconfig.cflags(LIBRARY).split(" "))]
    libs = [
        lib[2:]
        for lib in pkgconfig.libs(LIBRARY).split(" ")
        if not lib.startswith("-l")
    ]
    return cflags, libs


INCLUDE_DIRS, LIBRARY_DIRS = get_include_dirs()

ffibuilder = FFI()

cdefs = ""
dir_path = os.path.join(os.path.dirname(__file__), "headers/")
headers = [
    "base.h",
    "array.h",
    "file.h",
    "http.h",
    "ipp.h",
    "transcode.h",
    "pwg.h",
    "language.h",
    "cups.h",
    "dir.h",
    "dnssd.h",
    "form.h",
    "json.h",
    "jwt.h",
    "oauth.h",
    "raster.h",
]
print(dir_path)
for file in headers:
    file_path = os.path.join(dir_path, file)
    with open(file_path) as f:
        cdefs += f.read()

ffibuilder.cdef(cdefs)

ffibuilder.set_source(
    "cups._cups",
    r"""
    # include <cups/array.h>
    # include <cups/base.h>
    # include <cups/cups.h>
    # include <cups/dir.h>
    # include <cups/dnssd.h>
    # include <cups/file.h>
    # include <cups/form.h>
    # include <cups/http.h>
    # include <cups/ipp.h>
    # include <cups/json.h>
    # include <cups/jwt.h>
    # include <cups/language.h>
    # include <cups/oauth.h>
    # include <cups/ppd.h>
    # include <cups/pwg.h>
    # include <cups/raster.h>
    # include <cups/thread.h>
    # include <cups/transcode.h>
    # include <sys/types.h>
    # include <sys/stat.h>
    # include <stddef.h>
    # include <stdlib.h>
    # include <limits.h>
    # include <stdint.h>
    # include <stdarg.h>
    """,
    libraries=[LIBRARY],
    include_dirs=INCLUDE_DIRS,
    library_dirs=LIBRARY_DIRS,
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
