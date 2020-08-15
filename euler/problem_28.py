# -*- coding: utf-8 -*-
"""
Number spiral diagonals
=======================
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

       [21] 22  23  24 [25]
        20  [7]  8  [9] 10
        19   6  [1]  2  11
        18  [5]  4  [3] 12
       [17] 16  15  14 [13]

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""
from .utils import print_result


@print_result
def solve() -> int:
    last = 1001 * 1001
    total = 1
    step = 2
    i = 1
    while i < last:
        for _ in range(4):
            i += step
            total += i
        step += 2
    return total


if __name__ == "__main__":
    solve()
