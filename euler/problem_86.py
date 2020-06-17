# -*- coding: utf-8 -*-
"""
Cuboid route
============
https://projecteuler.net/problem=86

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
fly, F, sits in the opposite corner. By travelling on the surfaces of the room
the shortest "straight line" distance from S to F is 10 and the path is shown on
the diagram.

However, there are up to three "shortest" path candidates for any given cuboid
and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring
rotations, with integer dimensions, up to a maximum size of M by M by M, for
which the shortest route has integer length when M = 100. This is the least
value of M for which the number of solutions first exceeds two thousand; the
number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one
million.
"""
import math
from .utils import print_result, generate_triples

def min_cuboid_path(a: int, b:int, c:int):
    return math.sqrt(min(
        a ** 2 + (b + c) ** 2,
        b ** 2 + (a + c) ** 2,
        c ** 2 + (a + b) ** 2,
    ))

def generate_candidates(stop: int):
    for leg_1, leg_2, _ in generate_triples(stop):
        for a in range(1, leg_1 // 2 + 1):
            b = leg_1 - a
            c = leg_2
            yield tuple(sorted((a, b, c)))
        for a in range(1, leg_2 // 2 + 1):
            b = leg_2 - a
            c = leg_1
            yield tuple(sorted((a, b, c)))

@print_result
def solve():
    target = 2_000#1_000_000
    for a, b, c in sorted(set(generate_candidates(target)), key=max):
        if min_cuboid_path(a, b, c).is_integer():
            target -= 1
        if not target:
            return max(a, b, c)

if __name__ == "__main__":
    solve()
