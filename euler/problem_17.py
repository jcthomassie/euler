# -*- coding: utf-8 -*-
"""
Number letter counts
====================
https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""
from .utils import print_result

_FIRST = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
_TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}
_SECOND = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

FIRST = {k: len(v) for k, v in _FIRST.items()}
TEENS = {k: len(v) for k, v in _TEENS.items()}
SECOND = {k: len(v) for k, v in _SECOND.items()}
THIRD = {k: v + len("hundred") for k, v in FIRST.items()}
FOURTH = {k: v + len("thousand") for k, v in FIRST.items()}

AND = len("and")


def count_letters(n: int) -> int:
    digits = [int(s) for s in f"{n:04d}"]
    result = TEENS.get(int(f"{digits[-2]}{digits[-1]}"), 0)
    if not result:
        result += FIRST.get(digits[-1], 0)
        result += SECOND.get(digits[-2], 0)
    result += THIRD.get(digits[-3], 0)
    result += FOURTH.get(digits[-4], 0)
    if (digits[-2] or digits[-1]) and (digits[-4] or digits[-3]):
        result += AND
    return result


@print_result
def solve() -> int:
    num = 1000
    return sum(count_letters(n) for n in range(1, num + 1))


if __name__ == "__main__":
    solve()
