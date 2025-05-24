Build [libcups](https://github.com/OpenPrinting/libcups/) from source and either install it in a standard location or put the path of `libcups3.so.3` in `LD_LIBRARY_PATH`.

Then, install this from source using the command

`pip install -e .`

To test this, run the [`test.py`](test.py) file.

This binding is currently work in progress.

Currently implemented API is `cupsGetDests`.

This pyCups library is licensed under the Apache License Version 2.0.