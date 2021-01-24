# -*- coding: utf-8 -*-
"""
Maximum path sum II
===================
https://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

           3
          7 4
         2 4 6
        8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to
try every route to solve this problem, as there are 299 altogether! If you could
check one trillion (1012) routes every second it would take over twenty billion
years to check them all. There is an efficient algorithm to solve it. ;o)
"""
from pathlib import Path

from . import DATA_DIR
from .problem_18 import max_path_sum
from .utils import print_result


def scrape_pyramid(path: Path) -> list[list[int]]:
    """Scrape pyramid from text file into nested list of integers."""
    with path.open() as h:
        pyramid = []
        for line in h:
            pyramid.append([int(node) for node in line.strip().split()])
    return pyramid


@print_result
def solve() -> int:
    return max_path_sum(scrape_pyramid(DATA_DIR / "p067_triangle.txt"))


if __name__ == "__main__":
    solve()
