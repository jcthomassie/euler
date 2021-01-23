# -*- coding: utf-8 -*-
"""
Truncatable primes
==================
https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from typing import Iterator

from .utils import prime_mask, print_result

MAX = 750_000


def truncations(word: str) -> Iterator[str]:
    """Generate all truncations of the input word."""
    for i in range(1, len(word)):
        yield word[i:]  # left truncation
        yield word[:-i]  # right truncation


@print_result
def solve() -> int:
    results: list[int] = []
    primes = prime_mask(MAX)
    for n in range(11, MAX, 2):
        # Check number
        if not primes[n]:
            continue
        # Check truncations
        for trunc in truncations(f"{n}"):
            if not primes[int(trunc)]:
                break
        else:
            results.append(n)
            if len(results) == 11:
                return sum(results)
    raise RuntimeError("Failed to find solution")


if __name__ == "__main__":
    solve()
