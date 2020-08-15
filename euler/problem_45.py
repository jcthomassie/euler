# -*- coding: utf-8 -*-
"""
Triangular, pentagonal, and hexagonal
=====================================
https://projecteuler.net/problem=45

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
from typing import Iterator

from .utils import print_result


def generate_triangulars(n: int) -> Iterator[int]:
    """Generate triangular numbers starting from the Nth triangle number."""
    while True:
        yield n * (n + 1) // 2
        n += 1


def generate_pentagonals(n: int) -> Iterator[int]:
    """Generate pentagonal numbers starting from the Nth pentagonal number."""
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def generate_hexagonals(n: int) -> Iterator[int]:
    """Generate hexagonal numbers starting from the Nth hexagonal number."""
    while True:
        yield n * (2 * n - 1)
        n += 1


@print_result
def solve() -> int:
    generators = {
        "t": generate_triangulars(286),
        "p": generate_pentagonals(166),
        "h": generate_hexagonals(144),
    }
    values = {key: next(generator) for key, generator in generators.items()}
    while not values["t"] == values["p"] == values["h"]:
        smallest = min(values, key=values.get)
        values[smallest] = next(generators[smallest])
    return values["t"]


if __name__ == "__main__":
    solve()
