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

from .utils import prime_mask, print_result

MAX = 1_000_000


def rotations(word: str) -> Iterator[str]:
    """Generate all rotations of the input word."""
    for i in range(1, len(word)):
        yield word[i:] + word[:i]


@print_result
def solve() -> int:
    primes = prime_mask(MAX)
    count = 1  # include 2
    for n in range(3, MAX, 2):
        # Check number
        if not primes[n]:
            continue
        # Check rotations
        for rot in rotations(f"{n}"):
            if not primes[int(rot)]:
                break
        else:
            count += 1
    return count


if __name__ == "__main__":
    solve()
