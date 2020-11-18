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
from typing import Any, Iterator, List

from .utils import prime_mask, print_result


def four_digit_primes() -> Iterator[int]:
    """Generate all four-digit prime numbers."""
    primes = prime_mask(9999)
    for n in range(1001, 9999, 2):
        if primes[n]:
            yield n


def partitions(seq: List[Any]) -> Iterator[List[List[Any]]]:
    """Generate all possible partitions of the input list."""
    if not seq:
        yield []
    elif len(seq) == 1:
        yield [seq[:]]
    else:
        for i in range(1, len(seq) + 1):
            lhs = seq[:i]
            for rhs in partitions(seq[i:]):
                yield [lhs, *rhs]


@print_result
def solve() -> int:
    # Find all permutation groups
    perms = defaultdict(list)
    for prime in four_digit_primes():
        digits = tuple(sorted(f"{prime}"))
        perms[digits].append(prime)
    # Find evenly spaced 3-group
    for group in perms.values():
        if len(group) < 3:
            continue
        # Check all diffs for 3-run
        diffs = [b - a for a, b in zip(group, group[1:])]
        for part in partitions(diffs):
            for p_a, p_b in zip(part, part[1:]):
                if sum(p_a) == sum(p_b):
                    return group
    raise ValueError("Failed to find solution")


if __name__ == "__main__":
    solve()
