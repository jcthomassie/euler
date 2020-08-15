# -*- coding: utf-8 -*-
"""
Pandigital products
===================
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
import itertools

from .utils import print_result


@print_result
def solve() -> int:
    products = set()
    l_p = 4  # only works for products of length 4
    for perm in itertools.permutations("123456789"):
        p = int("".join(perm[:l_p]))
        for l_a, l_b in ((3, 2), (4, 1)):
            a = int("".join(perm[l_p : l_p + l_a]))
            b = int("".join(perm[l_p + l_a :]))
            if p == a * b:
                products.add(p)
                break
    return sum(products)


if __name__ == "__main__":
    solve()
