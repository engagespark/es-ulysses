import logging

from mock import patch

from logic import log_sometimes, rst_quote, shorten


logging.basicConfig()
log = logging.getLogger()


def test_result_of_shortening_is_logged():
    """The shorten function always logs its results as debug."""
    with patch.object(log, "debug") as debug:
        shorten("1234567890")
        debug.assert_called_with("12345")


def test_log_for_one_arg():
    """Only log, when at most one argument is given."""
    with patch.object(log, "debug") as debug:
        log_sometimes(1)
        log_sometimes(2, 3)
        log_sometimes(4)
        log_sometimes(5, 6, 7)
        log_sometimes(8, 9, 10, 11)
        debug.assert_any_call("1")
        debug.assert_any_call("4")
        assert debug.call_count == 2


def test_prefix_without_error():
    """When a string is given, it is quoted just fine."""
    assert rst_quote("hello!") == "| hello!"


def test_prefix_with_error():
    """When something unquotable is given, return an empty, quoted line."""
    assert rst_quote(1) == "| "
