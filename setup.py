from setuptools import setup

setup(
    cffi_modules=["cups/build_cups.py:ffibuilder"],
)
