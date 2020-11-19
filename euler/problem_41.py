# -*- coding: utf-8 -*-
"""
Pandigital prime
================
https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""
import itertools

from .utils import is_prime, print_result


def largest_pandigital_prime(n: int = 4) -> int:
    """Find largest n-digit pandigital prime."""
    # Get test domain
    digits = "123456789"[:n]
    # Find largest pandigital that is prime
    for perm in itertools.permutations(digits[::-1]):
        pandigital = int("".join(perm))
        if is_prime(pandigital):
            return pandigital
    raise RuntimeError("Failed to find solution")


@print_result
def solve() -> int:
    return largest_pandigital_prime(7)


if __name__ == "__main__":
    solve()
