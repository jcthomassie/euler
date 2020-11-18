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
from typing import List

from .utils import prime_mask, print_result


def four_digit_primes() -> List[int]:
    fdp = []
    primes = prime_mask(9999)
    for n in range(1001, 9999, 2):
        if primes[n]:
            fdp.append(n)
    return fdp


@print_result
def solve() -> int:
    fdp = four_digit_primes()
    # Find all permutation groups
    perms = defaultdict(list)
    for prime in fdp:
        perms[tuple(sorted(f"{prime}"))].append(prime)
    # Drop all groups that are too short
    for group in perms.values():
        if len(group) < 3:
            continue
        diffs = [b - a for a, b in zip(group, group[1:])]
        print(diffs)
    raise ValueError("Failed to find solution")


if __name__ == "__main__":
    solve()
