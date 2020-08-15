# -*- coding: utf-8 -*-
"""
Lexicographic permutations
==========================
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import functools

from .utils import print_result


@functools.lru_cache(10, typed=True)
def factorial(n):
    """
    Compute the factorial of natural number n.
    """
    if n in (1, 0):
        return 1
    return n * factorial(n - 1)


@print_result
def solve():
    target = 1000000
    total = 0
    digits = list(range(10))
    result = ""
    for n in digits[::-1]:
        m = 1
        while total + factorial(n) < target:
            m += 1
            total += factorial(n)
        result += str(digits.pop(m - 1))
    return result


if __name__ == "__main__":
    solve()
