# -*- coding: utf-8 -*-
"""
Amicable numbers
================
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import numpy as np

from .utils import print_result


def divisor_sums(n):
    """
    Generate a flat array of the sums of the proper divisors of all numbers less
    than n.
    """
    sums = np.zeros(n, dtype=int)
    for i in range(1, n):
        j = 2 * i
        while j < n:
            sums[j] += i
            j += i
    return sums


@print_result
def solve():
    n = 10000
    sums = divisor_sums(n)
    total = 0
    for a, b in enumerate(sums):
        if b < n and b != a and sums[b] == a:
            total += a
    return total


if __name__ == "__main__":
    solve()
