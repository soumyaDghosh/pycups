from setuptools import setup, find_packages

setup(
    name="cups",
    version="0.1.0",
    description="Python bindings and helpers for libcups",
    author="Soumyadeep Ghosh",
    author_email="soumyadeepghosh2004@zohomail.in",
    packages=find_packages(),  # automatically finds cups/ and subpackages
    install_requires=[
        "cffi>=1.17.1",
    ],
    cffi_modules=["package/build_ffi.py:ffibuilder"],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries",
    ],
)
