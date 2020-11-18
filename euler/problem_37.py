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
from functools import lru_cache
from typing import Iterator, List

from .utils import is_prime, print_result


def truncations(word: str) -> Iterator[str]:
    for i in range(1, len(word)):
        yield word[i:]  # left truncation
        yield word[:-i]  # right truncation


@lru_cache
def is_prime_str(word: str) -> bool:
    return is_prime(int(word))


@print_result
def solve() -> int:
    truncatables: List[int] = []
    n = 11
    while len(truncatables) < 11:
        if is_prime(n):
            for trunc in truncations(f"{n}"):
                if not is_prime_str(trunc):
                    break
            else:
                truncatables.append(n)
        n += 2
    return sum(truncatables)


if __name__ == "__main__":
    solve()
