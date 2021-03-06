# -*- coding: utf-8 -*-
"""
Double-base palindromes
=======================
https://projecteuler.net/problem=36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""
from .problem_4 import is_palindrome
from .utils import print_result


@print_result
def solve() -> int:
    return sum(
        n for n in range(1000000) if is_palindrome(f"{n}") and is_palindrome(bin(n)[2:])
    )


if __name__ == "__main__":
    solve()
