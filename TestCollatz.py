#!/usr/bin/env python3

# --------------
# TestCollatz.py
# --------------

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------

from io import BytesIO as StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(1, 999999)  # to check if the range is too big
        self.assertEqual(v, 525)

    def test_eval_6(self):
        v = collatz_eval(
            10, 1
        )  # to check if the first input is bigger than the second one
        self.assertEqual(v, 20)

    def test_eval_7(self):
        v = collatz_eval(1, 1)  # to check if the first input and second input are same
        self.assertEqual(v, 1)

    def test_eval_8(self):
        v = collatz_eval(3, 7)
        self.assertEqual(v, 17)

    def test_eval_9(self):
        v = collatz_eval

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 0, 10, 20)
        self.assertEqual(w.getvalue(), "0 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n"
        )

    def test_solve_2(self):
        r = StringIO("1 10\n10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n10 10 7\n")


# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()


"""
$ coverage run TestCollatz.py
..............
----------------------------------------------------------------------
Ran 14 tests in 16.397s

OK



$ coverage report -m
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
Collatz.py          46      0   100%
TestCollatz.py      53      0   100%
----------------------------------------------
TOTAL               99      0   100%


"""
