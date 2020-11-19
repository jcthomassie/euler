# -*- coding: utf-8 -*-
"""
Pandigital multiples
====================
https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import itertools

from .utils import print_result


def concatenated_product(n_str: str) -> bool:
    """Return True if the input number is a 'concatenated product'."""
    # Check all prefixes
    for i in range(1, len(n_str) // 2 + 1):
        seed = int(n_str[:i])
        term = 1
        rhs = n_str[i:]
        while rhs:
            term += 1
            lhs = f"{term * seed}"
            if rhs.startswith(lhs):
                rhs = rhs[len(lhs) :]
            else:
                break
        else:
            return True
    return False


@print_result
def solve() -> int:
    for perm in itertools.permutations("987654321"):
        pandigital = "".join(perm)
        if concatenated_product(pandigital):
            return int(pandigital)
    raise ValueError("Failed to find solution")


if __name__ == "__main__":
    solve()
