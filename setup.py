from setuptools import setup  # type: ignore[reportMissingModuleSource]  # noqa: D100

setup(
    cffi_modules=["cups/build_cups.py:ffibuilder"],
)
