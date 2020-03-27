#!/usr/bin/env python3

# ----------
# Collatz.py
# ----------

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------

# from typing import IO, List

# ------------
# collatz_read
# ------------
# -> List[int]

"""
Collatz.py by Jiwon Lee
EID : jl74566

declare the global array, memory.
memory is an array with 3,000,000 elements.
all elements are initialized with zero at first.
"""
memory = [0] * 3000000  # global memory. init with zero with 3000000 elements


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    # s = list(map(int, s))
    a = s.split()
    if len(a) == 1:
        a.append(a[0])
    assert len(a) == 2
    return [int(a[0]), int(a[1])]


# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    if i is bigger than j, swap them to make the for loop run normally.

    max_val is initialized to zero. max_val is the max cycle length in the range
    using the global array 'memory'.

    iterator is the value being checked.

    if iterator has been calculated before,
    the element in the memory array with the index of iterator won't be zero.

    if iterator has not been calculated before, keep computing.

    after computing, check the memory array
    if the computed value has been calculated for the cycle length before.

    compare the current maximum value with cycle length of the iterator.

    return the current maximum value
    after computing all the values in the range through for loop
    """
    i = int(i)
    j = int(j)

    if i > j:  # if first input is bigger than second one, swap
        i, j = j, i

    assert i > 0
    assert memory[0] == 0
    max_val = 0  # init maximum value with zero

    for iterator in range(i, j + 1):
        count = 1
        if memory[iterator] != 0:
            count = memory[iterator]
        else:
            n = iterator
            assert memory[n] == 0
            while n > 1:
                if n % 2 == 0:
                    n = n // 2
                    assert isinstance(n, int)
                else:
                    n = n * 3 + 1

                if n < 3000000 and memory[n] != 0:  # has been computed before
                    assert memory[n] != None
                    count = count + memory[n]
                    break
                else:  # has not been computed before
                    count = count + 1

            memory[iterator] = count

        if max_val < count:  # compare with the current maximum value.
            max_val = count

    return max_val


# -------------
# collatz_print
# -------------

# def collatz_print (w: IO[str], i: int, j: int, v: int) -> None :
def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    assert isinstance(i, int)
    assert isinstance(j, int)
    assert isinstance(v, int)

    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")


# -------------
# collatz_solve
# -------------

# def collatz_solve (r: IO[str], w: IO[str]) -> None :
def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """

    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
