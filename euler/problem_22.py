# -*- coding: utf-8 -*-
"""
Names scores
============
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import os

from . import DATA_DIR
from .utils import print_result


def scrape_names(path: str):
    """
    Scrape names into a list and sort them.
    """
    with open(path, "r") as h:
        return sorted(eval(next(h)))


def name_score(name: str) -> int:
    """
    Get the score of the input name.
    """
    return sum(ord(char) - 64 for char in name)  # 64 == ord("A") - 1


@print_result
def solve():
    path = os.path.join(DATA_DIR, "p022_names.txt")
    total = 0
    for i, name in enumerate(scrape_names(path), start=1):
        total += i * name_score(name)
    return total


if __name__ == "__main__":
    solve()
