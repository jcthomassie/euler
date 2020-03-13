"""
Prime pair sets
===============
https://projecteuler.net/problem=60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""
from utils import print_result, prime_mask

def int_concat(a, b):
    return int(f"{a}{b}")

@print_result
def solve():
    n = 4
    p_max = 1000000
    mask = prime_mask(p_max)
    passed = [3]
    for i in range(5, p_max):
        if mask[i]:
            for j in passed:
                if not mask[int_concat(i, j)] or not mask[int_concat(j, i)]:
                    break
            else:
                passed.append(i)
                if len(passed) >= n:
                    break
    return sum(passed)

if __name__ == "__main__":
    solve()
