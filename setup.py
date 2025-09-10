from setuptools import setup  # noqa: D100

setup(
    cffi_modules=["cups/build_cups.py:ffibuilder"],
)
