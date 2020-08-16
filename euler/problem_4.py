# -*- coding: utf-8 -*-
"""
Largest palindrome product
==========================
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from .utils import print_result


def is_palindrome(s: str) -> bool:
    """Return True if input string is palindrome."""
    return s == s[::-1]


@print_result
def solve() -> int:
    res = 0
    for n in range(999, 100, -1):
        for m in range(n, 100, -1):
            prod = m * n
            if is_palindrome(f"{prod}"):
                res = max(res, prod)
    return res


if __name__ == "__main__":
    solve()
