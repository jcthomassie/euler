# -*- coding: utf-8 -*-
"""
Path sum: four ways
===================
https://projecteuler.net/problem=83

NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
right, by moving left, right, up, and down, is indicated in bold red and is
equal to 2297.

        [131]  673  [234] [103] [ 18]

        [201] [ 96] [342]  965  [150]

         630   803   746  [422] [111]

         537   699   497  [121]  956

         805   732   524  [ 37] [331]

Find the minimal path sum from the top left to the bottom right by moving left,
right, up, and down in matrix.txt (right click and "Save Link/Target As..."), a
31K text file containing an 80 by 80 matrix.
"""
import os

from . import DATA_DIR
from .problem_81 import a_star, scrape_array
from .utils import print_result


@print_result
def solve():
    return sum(a_star(scrape_array(os.path.join(DATA_DIR, "p083_matrix.txt")),))


if __name__ == "__main__":
    solve()
