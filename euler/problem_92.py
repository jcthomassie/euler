# -*- coding: utf-8 -*-
"""
Square digit chains
===================
https://projecteuler.net/problem=92

A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1

85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
import functools

from .utils import print_result


@functools.lru_cache
def find_cycle(n: int) -> int:
    if n in (1, 89):
        return n
    return find_cycle(sum(int(d) ** 2 for d in f"{n}"))


@print_result
def solve() -> int:
    count = 0
    for n in range(1, 10_000_000):
        if find_cycle(n) == 89:
            count += 1
    return count


if __name__ == "__main__":
    solve()
