# -*- coding: utf-8 -*-
"""
Champernowne's constant
=======================
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from .utils import print_result


def champernowne_count(n: int) -> int:
    """Get the number of digits produced by numbers of length n."""
    return 9 * n * 10 ** (n - 1)  # type: ignore


def champernowne_length(x: int) -> int:
    """Get the length of Champernowne's constant up through X."""
    n = len(f"{x}")
    return sum(champernowne_count(m) for m in range(1, n)) + n * (x - 10 ** (n - 1) + 1)


def champernowne_digit(n: int) -> int:
    """Get the Nth digit of Champernowne's constant."""
    pass


@print_result
def solve() -> int:
    raise NotImplementedError()


if __name__ == "__main__":
    solve()
