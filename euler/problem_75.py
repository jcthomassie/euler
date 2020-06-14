# -*- coding: utf-8 -*-
"""
Singular integer right triangles
================================
https://projecteuler.net/problem=75

It turns out that 12 cm is the smallest length of wire that can be bent to form
an integer sided right angle triangle in exactly one way, but there are many
more examples.

    12 cm: (3,4,5)
    24 cm: (6,8,10)
    30 cm: (5,12,13)
    36 cm: (9,12,15)
    40 cm: (8,15,17)
    48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer
sided right angle triangle, and other lengths allow more than one solution to be
found; for example, using 120 cm it is possible to form exactly three different
integer sided right angle triangles.

    120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can
exactly one integer sided right angle triangle be formed?
"""
import collections
import math
from .utils import print_result

@print_result
def solve():
    # Build list of side lengths
    limit = 1500000
    sides = list(range(1, limit // 2 + 1))
    squares = [None] + [s ** 2 for s in sides]
    counts = collections.Counter()
    while sides:
        a = sides.pop()
        for b in sides:
            c = math.sqrt(squares[a] + squares[b])
            if a + b + c > limit:
                break
            if c.is_integer():
                counts[int(a + b + c)] += 1
    return sum(1 for c in counts.values() if c == 1)

if __name__ == "__main__":
    solve()
