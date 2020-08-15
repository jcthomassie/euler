# -*- coding: utf-8 -*-
"""
Digit factorials
================
https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

NOTE: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from .problem_24 import factorial
from .utils import print_result


def get_upper_bound() -> int:
    """
    An easy upper bound for the largest number that is the sum of the factorial
    of its digits can be found using the following logic:

        let B be the bound, and N be the number of digits in B...

        9! * N < B

    The bound can then be improved to:

        9! * (N - 1)
    """
    digits = 2
    while 10 ** (digits - 1) < factorial(9) * digits:
        digits += 1
    return factorial(9) * (digits - 1)


@print_result
def solve() -> int:
    digit_factorials = {str(d): factorial(d) for d in range(10)}
    total = 0
    for n in range(10, get_upper_bound()):
        if n == sum(digit_factorials[d] for d in str(n)):
            total += n
    return total


if __name__ == "__main__":
    solve()
