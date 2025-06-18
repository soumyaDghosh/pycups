### Building

Build [libcups](https://github.com/OpenPrinting/libcups/) from source and either install it in a standard location or put the path of `libcups3.so.3` in `LD_LIBRARY_PATH`.

Then, install this from source using the command

`pip install -e .`

### Testing

To test this, run the [`test/test.py`](test/test.py) file. We cannot test `addDests` and `setDests` without doing destructive changes in the system, so they're not yet added in the test. This is a proof-of-concept test. So, please run it with caution.

This binding is currently work in progress.

### APIs

Currently implemented APIs are:

- #### Dests
    - `cupsAddDests`
    - `cupsCopyDest`
    - `cupsGetDests`
    - `cupsGetDestWithURI`
    - `cupsSetDests`
    - `cupsAddDests`

- #### Options
    - `cupsGetOption`


### License

This pyCups library is licensed under the Apache License Version 2.0.
