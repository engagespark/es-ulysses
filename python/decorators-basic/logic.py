# DO NOT CHANGE THIS FILE TO COMPLETE THE CHALLENGE.
"""Usage of the decorators."""

import logging

from deco import ignore, log_result, skip


log = logging.getLogger()


@log_result
def shorten(long_line):
    """Shortens the line to a certain maximum length.

    Logs the results.

    """
    return long_line[:5]


@skip(when=lambda args, kw: len(args) > 1)
def log_sometimes(*args):
    """Log the argument as debug, but only when at most 1 is given."""
    log.debug(" | ".join(map(str, args)))


@ignore(TypeError, retry_with="")
def rst_quote(s):
    """Quotes a one-line string in ReSTructured format.

    For non-strings, an empty quoted line is returned.

    """
    return "| " + s
