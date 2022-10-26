# -*- coding: utf-8 -*-
"""
Quadratic primes
================
https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer
values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) +
41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
primes for the consecutive values 0 <= n <= 79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b,

    where |a| < 1000 and |b| <= 1000
    where |n| is the absolute value of n

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""
import functools

import numpy as np

from .utils import prime_mask, print_result


def func(n: int, a: int, b: int) -> int:
    return n**2 + a * n + b


@functools.lru_cache
def primes() -> np.ndarray:
    return prime_mask(func(1000, 1000, 1000))


@functools.lru_cache()
def depth(a: int, b: int) -> int:
    """Return the number of consecutive N that produce a prime for func(n, a, b)."""
    n = 0
    while primes()[func(n, a, b)]:
        n += 1
    return n


@print_result
def solve() -> int:
    d_max = 0
    best = None
    for b in range(-999, 1001, 2):
        # B must be prime to satisfy f(n=0)
        if not primes()[b]:
            continue
        for a in range(-999, 1000):
            if depth(a, b) > d_max:
                best = (a, b)
                d_max = depth(a, b)
    if best is None:
        raise RuntimeError("Failed to find solution")
    return best[0] * best[1]


if __name__ == "__main__":
    solve()
