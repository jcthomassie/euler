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
from .utils import prime_mask, print_result


def largest_pandigital_prime(n: int = 4) -> int:
    """Generate all nine-digit prime numbers that might be pandigital."""
    # Get test domain
    digits = "123456789"[:n]
    n_min = int(digits)
    n_max = int(digits[::-1]) | 1
    comp = set(digits)
    # Find largest prime that is pandigital
    primes = prime_mask(n_max + 1)
    for n in range(n_max, n_min, -2):
        if primes[n] and set(f"{n}") == comp:
            return n
    raise RuntimeError("Failed to find solution")


@print_result
def solve() -> int:
    return largest_pandigital_prime(7)


if __name__ == "__main__":
    solve()
