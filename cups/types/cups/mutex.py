from cups.types.base import cupsBaseClass, _lib

class cupsMutex(cupsBaseClass):
    ffi_name = "cups_mutex_t"

    def __init__(self):
        super().__init__()
        _lib.cupsMutexInit(self.ffi_value)

    def __del__(self):
        _lib.cupsMutexDestroy(self.ffi_value)

    def lock(self):
        _lib.cupsMutexLock(self.ffi_value)

    def unlock(self):
        _lib.cupsMutexUnlock(self.ffi_value)
