# -*- coding: utf-8 -*-
"""
Distinct primes factors
=======================
https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""
from functools import lru_cache
from typing import Tuple

from .utils import prime_mask, print_result

MAX = 150_000


@print_result
def solve() -> int:
    mask = prime_mask(MAX)
    primes = [2, *(i for i in range(3, MAX, 2) if mask[i])]

    @lru_cache
    def prime_factors(n: int) -> Tuple[int, ...]:
        """Compute the prime factors of the input integer."""
        if mask[n] or n == 1:
            return (n,)
        for m in primes:
            if n % m == 0:
                return (m, *prime_factors(n // m))
        raise RuntimeError(f"Failed to factorize {n}")

    # Look for N consecutive integers with N distinct prime factors
    count = 4
    for i in range(2, MAX):
        for j in range(i, i + count):
            if len(set(prime_factors(j))) != count:
                break
        else:
            return i
    raise RuntimeError("Failed to find solution")


if __name__ == "__main__":
    solve()
