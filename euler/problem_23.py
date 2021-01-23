# -*- coding: utf-8 -*-
"""
Non-abundant sums
=================
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""
from .problem_21 import divisor_sums
from .utils import print_result


def abundant_numbers(n: int) -> list[int]:
    """Get all abundant numbers below n."""
    abundant = []
    for a, b in enumerate(divisor_sums(n)):
        if b > a:
            abundant.append(a)
    return abundant


def abundant_sums(n: int) -> set[int]:
    """Get all integers below n that can be written as the sum of two abundant numbers."""
    abundant = abundant_numbers(n)
    sums = set()
    for i, a in enumerate(abundant):
        for b in abundant[i:]:
            s = a + b
            if s > n:
                break
            sums.add(s)
    return sums


@print_result
def solve() -> int:
    n = 28123
    return sum(set(range(n)) - abundant_sums(n))


if __name__ == "__main__":
    solve()
