# -*- coding: utf-8 -*-
"""
Prime permutations
==================
https://projecteuler.net/problem=49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from collections import defaultdict
from typing import Iterator

from .utils import prime_mask, print_result


def four_digit_primes() -> Iterator[int]:
    """Generate all four-digit prime numbers."""
    primes = prime_mask(9999)
    for n in range(1001, 9999, 2):
        if primes[n]:
            yield n


@print_result
def solve() -> int:
    # Find all permutation groups
    perms = defaultdict(list)
    for prime in four_digit_primes():
        digits = tuple(sorted(f"{prime}"))
        perms[digits].append(prime)
    # Drop example group
    del perms[tuple("1478")]
    # Find evenly spaced 3-group
    for group in perms.values():
        if len(group) < 3:
            continue
        # Check all 3-groups
        for i, a in enumerate(group, start=1):
            for j, b in enumerate(group[i:], start=1):
                for c in group[i + j:]:
                    # Evenly spaced
                    if (b - a) == (c - b):
                        return int(f"{a}{b}{c}")
    raise ValueError("Failed to find solution")


if __name__ == "__main__":
    solve()
