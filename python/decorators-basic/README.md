# Decorator Basics

Learn about decorators.

This challenge is just about simple function decorators.
You'll learn how to write one, and give it arguments.

## The Challenge

Fix the tests.

Implement the decorators in `deco.py`.
They are used in `logic.py`. Do not change that file.

## Setup

Create the virtualenv and download dependencies.

    make setup

## Run the tests

Run the tests.

    make test

## Examples

Run the `main.py` to easily experiment with the functions.

    $ ./main.py
    [shorten] Shortening long string this is a long string to be shortened -> this

    [log_sometimes] Logging ('one', 'two', 'three') ...
    [log_sometimes] Logging ('four',) ...
    DEBUG:root:four
    [log_sometimes] Logging (7,) ...
    DEBUG:root:7
    [log_sometimes] Logging whynot ...
    Done logging.

    [rst_quote] Quoting blub -> | blub
