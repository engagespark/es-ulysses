# IMPLEMENT THE DECORATORS IN THIS FILE.
import logging

log = logging.getLogger()


def ignore(clazz, **kw):
    """Ignore exceptions of the given type and retry with the given string.

    Decorates a function with a string as first argument.

    """
    pass


def log_result():
    pass


def skip(when):
    """Skip the function call when the predicate function yields true.

    The `when` function is given two arguments: the *args list and the **kw
    dictionary. Whenn it returns true, the decorated function is not called.
    Instead, None is returned.

    """
    def dec():
        pass
