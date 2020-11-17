# -*- coding: utf-8 -*-
"""
Circular primes
===============
https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""
from typing import Iterator

from .utils import prime_list, print_result

MAX = 1_000_000


def rotations(word: str) -> Iterator[str]:
    """Generate all rotations of the input word."""
    yield word
    for i in range(1, len(word)):
        yield word[i:] + word[:i]


@print_result
def solve() -> int:
    primes = set(prime_list(MAX))
    count = 0
    for prime in primes:
        family = set(int(rot) for rot in rotations(str(prime)))
        if family.issubset(primes):
            count += 1
    return count


if __name__ == "__main__":
    solve()
