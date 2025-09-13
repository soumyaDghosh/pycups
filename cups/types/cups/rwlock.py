from cups.types.base import cupsBaseClass, _lib

class cupsRWLock(cupsBaseClass):
    ffi_name = "cups_rwlock_t"

    def __init__(self, args=None):
        if args and self._is_valid_ctype(args):
            self.ffi_value = args
        else:
            super().__init__(args)
            _lib.cupsRWInit(self.ffi_value)

    def lockRead(self) -> None:
        _lib.cupsRWLockRead(self.ffi_value)

    def lockWrite(self) -> None:
        _lib.cupsRWLockWrite(self.ffi_value)

    def unlock(self) -> None:
        _lib.cupsRWUnlock(self.ffi_value)

    def __del__(self):
        _lib.cupsRWDestroy(self.ffi_value)

