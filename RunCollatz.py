#!/usr/bin/env python3

# -------------
# RunCollatz.py
# -------------

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------

from sys import stdin, stdout
from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(stdin, stdout)
