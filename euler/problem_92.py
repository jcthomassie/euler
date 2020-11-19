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


def sum_digit_squares(n: int) -> int:
    result = 0
    while n:
        n, mod = divmod(n, 10)
        result += mod * mod
    return result


@functools.lru_cache
def is_cycle_89(n: int) -> bool:
    if n == 1:
        return False
    if n == 89:
        return True
    return is_cycle_89(sum_digit_squares(n))


@print_result
def solve() -> int:
    return sum(is_cycle_89(n) for n in range(1, 10_000_000))


if __name__ == "__main__":
    solve()
