#!/usr/bin/env python
from __future__ import print_function
import logging

import logic


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    longstring = "this is a long string to be shortened"
    print("[{name}] Shortening long string {} -> {}".format(
        longstring, logic.shorten(longstring), name=logic.shorten.__name__))

    print()
    messages = [("one", "two", "three"), ("four",), (7,), ("whynot")]
    for args in messages:
        print("[{name}] Logging {} ...".format(
            args,
            name=logic.log_sometimes.__name__),
        )
        logic.log_sometimes(*args)
    print("Done logging.")

    print()
    print("[{name}] Quoting {} -> {}".format(
        "blub", logic.rst_quote("blub"), name=logic.rst_quote.__name__))
