from cffi import FFI
import pkgconfig

LIBRARY = "cups3"
VERSION = "3.0.0"

def get_include_dirs():
    include_dirs, lib_dirs = [], []
    if not (pkgconfig.installed(LIBRARY, f"<={VERSION}")):
        raise Exception("Cannot find pkg-config file for cups3.\nIs CUPS 3.0 development libraries properly installed?")
    cflags = [c[2:] for c in (pkgconfig.cflags(LIBRARY).split(" "))]
    libs = [lib[2:] for lib in pkgconfig.libs(LIBRARY).split(" ") if not lib.startswith("-l")]
    return cflags, libs

INCLUDE_DIRS, LIBRARY_DIRS = get_include_dirs()

ffibuilder = FFI()

ffibuilder.cdef("""
    typedef struct _http_s http_t;

    typedef struct {
        char *name;
        char *value;
    } cups_option_t;

    typedef struct {
        char *name, *instance;
        _Bool is_default;
        size_t num_options;
        cups_option_t *options;
    } cups_dest_t;
            
    enum cups_ptype_e			// Printer type/capability flags
    {
        CUPS_PTYPE_LOCAL = 0x0000,			// Local printer or class
        CUPS_PTYPE_CLASS = 0x0001,			// Printer class
        CUPS_PTYPE_REMOTE = 0x0002,			// Remote printer or class
        CUPS_PTYPE_BW = 0x0004,			// Can do B&W printing
        CUPS_PTYPE_COLOR = 0x0008,			// Can do color printing
        CUPS_PTYPE_DUPLEX = 0x0010,			// Can do two-sided printing
        CUPS_PTYPE_STAPLE = 0x0020,			// Can staple output
        CUPS_PTYPE_COPIES = 0x0040,			// Can do copies in hardware
        CUPS_PTYPE_COLLATE = 0x0080,			// Can quickly collate copies
        CUPS_PTYPE_PUNCH = 0x0100,			// Can punch output
        CUPS_PTYPE_COVER = 0x0200,			// Can cover output
        CUPS_PTYPE_BIND = 0x0400,			// Can bind output
        CUPS_PTYPE_SORT = 0x0800,			// Can sort output
        CUPS_PTYPE_SMALL = 0x1000,			// Can print on Letter/Legal/A4-size media
        CUPS_PTYPE_MEDIUM = 0x2000,			// Can print on Tabloid/B/C/A3/A2-size media
        CUPS_PTYPE_LARGE = 0x4000,			// Can print on D/E/A1/A0-size media
        CUPS_PTYPE_VARIABLE = 0x8000,			// Can print on rolls and custom-size media
        CUPS_PTYPE_DEFAULT = 0x20000,			// Default printer on network
        CUPS_PTYPE_FAX = 0x40000,			// Fax queue
        CUPS_PTYPE_REJECTING = 0x80000,		// Printer is rejecting jobs
        CUPS_PTYPE_NOT_SHARED = 0x200000,		// Printer is not shared
        CUPS_PTYPE_AUTHENTICATED = 0x400000,		// Printer requires authentication
        CUPS_PTYPE_COMMANDS = 0x800000,		// Printer supports maintenance commands
        CUPS_PTYPE_DISCOVERED = 0x1000000,		// Printer was discovered
        CUPS_PTYPE_SCANNER = 0x2000000,		// Scanner-only device
        CUPS_PTYPE_MFP = 0x4000000,			// Printer with scanning capabilities
        CUPS_PTYPE_FOLD = 0x10000000,			// Can fold output
        CUPS_PTYPE_OPTIONS = 0x1006fffc		// ~(CLASS | REMOTE | IMPLICIT | DEFAULT | FAX | REJECTING | DELETE | NOT_SHARED | AUTHENTICATED | COMMANDS | DISCOVERED) @private@
    };
    typedef unsigned cups_ptype_t;		// Combined printer type/capability flags

    enum cups_dest_flags_e			// Flags for @link cupsConnectDest@ and @link cupsEnumDests@
    {
        CUPS_DEST_FLAGS_NONE = 0x00,			// No flags are set
        CUPS_DEST_FLAGS_UNCONNECTED = 0x01,		// There is no connection
        CUPS_DEST_FLAGS_MORE = 0x02,			// There are more destinations
        CUPS_DEST_FLAGS_REMOVED = 0x04,		// The destination has gone away
        CUPS_DEST_FLAGS_ERROR = 0x08,			// An error occurred
        CUPS_DEST_FLAGS_RESOLVING = 0x10,		// The destination address is being resolved
        CUPS_DEST_FLAGS_CONNECTING = 0x20,		// A connection is being established
        CUPS_DEST_FLAGS_CANCELED = 0x40,		// Operation was canceled
        CUPS_DEST_FLAGS_DEVICE = 0x80			// For @link cupsConnectDest@: Connect to device
    };
    typedef unsigned cups_dest_flags_t;

    typedef bool (*cups_dest_cb_t)(void *user_data, cups_dest_flags_t flags, cups_dest_t *dest);

    size_t cupsGetDests(http_t *http, cups_dest_t **dests);
    void cupsFreeDests(size_t num_dests, cups_dest_t *dests);
    bool cupsEnumDests(unsigned flags, int msec, int *cancel, cups_ptype_t type, cups_ptype_t mask, cups_dest_cb_t cb, void *cb_data);
""")

ffibuilder.set_source(
    "cups._cups",
    '#include <cups/cups.h>',
    libraries=[LIBRARY],
    include_dirs=INCLUDE_DIRS,
    library_dirs=LIBRARY_DIRS,
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
