# -*- coding: utf-8 -*-
"""
Even Fibonacci numbers
======================
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""
import functools

from .utils import print_result


@functools.lru_cache(1000000, typed=True)
def fibonacci(n: int) -> int:
    """Compute the N-th fibonacci number."""
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@print_result
def solve() -> int:
    total = 0
    n = 2
    while True:
        value = fibonacci(n)
        if value > 4000000:
            break
        total += value
        n += 3
    return total


if __name__ == "__main__":
    solve()
