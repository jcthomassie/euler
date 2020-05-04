"""
Digit cancelling fractions
==========================
https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""
from .utils import print_result

def gcd(a, b):
    """
    Returns the GCD (Greatest Common Divisor) of integers a and b.
    """
    while b:
        a, b = b, a % b
    return a

def simplify(a, b):
    """
    Simplifies the fraction a / b by dividing out the GCD.
    """
    d = gcd(a, b)
    return a // d, b // d

@print_result
def solve():
    p_a = 1
    p_b = 1
    for b in range(10, 100):
        if b % 10 == 0:
            continue
        for a in range(10, b):
            if a % 10 == 0:
                continue
            # Remove common digit
            a_dig = list(str(a))
            b_dig = list(str(b))
            try:
                drop = (set(a_dig) & set(b_dig)).pop()
                a_dig.remove(drop)
                b_dig.remove(drop)
            except KeyError:
                continue
            # See if reduced fraction matches
            a_r = int(a_dig[0])
            b_r = int(b_dig[0])
            if a_r / b_r == a / b:
                p_a *= a
                p_b *= b
    return simplify(p_a, p_b)[-1]

if __name__ == "__main__":
    solve()
