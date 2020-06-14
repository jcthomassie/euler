# -*- coding: utf-8 -*-
"""
Coin sums
=========
https://projecteuler.net/problem=31

In the United Kingdom the currency is made up of pound (£) and pence (p). There
are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
from .utils import print_result

def make_change(target, values):
    count = 0
    while values:
        v = values.pop()
        i = 1
        while i * v < target:
            count += make_change(target - i * v, values[:])
            i += 1
        else:
            if i * v == target:
                count += 1
    return count

@print_result
def solve():
    return make_change(
        200,
        [1, 2, 5, 10, 20, 50, 100, 200]
    )

if __name__ == "__main__":
    solve()
