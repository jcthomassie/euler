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
from collections import defaultdict

from .utils import print_result, prime_mask

P_MAX = 100000000
P_MASK = prime_mask(P_MAX)


def sub_primes(n: int):
    """
    Yield all pairs of 'substring' primes for the input integer.
    """
    s = str(n)
    for i in range(1, len(s)):
        if "0" in (s[0], s[i]):
            continue
        a = int(s[:i])
        b = int(s[i:])
        c = int(s[i:] + s[:i])
        if P_MASK[a] and P_MASK[b] and P_MASK[c]:
            yield a, b

def generate_tree():
    """
    Build tree of all pairs of 'substring' primes in the prime table.
    """
    tree = defaultdict(set)
    for n, is_prime in enumerate(P_MASK):
        if is_prime:
            for a, b in sub_primes(n):
                tree[a].add(b)
                tree[b].add(a)
    return tree

def find_cliques(tree, size=5):
    """
    Find all cliques of the specified size in the input graph.
    """
    len_neighbors = lambda n: len(tree[n])
    # smallest vertex -> largest vertex
    for node in sorted(tree.keys(), key=len_neighbors, reverse=True):
        clique = set((node,))
        for neighbor in sorted(tree[node], key=len_neighbors, reverse=True):
            if len(tree[neighbor]) >= size and clique.issubset(tree[neighbor]):
                clique.add(neighbor)
                if len(clique) == size:
                    yield clique
                    break

@print_result
def solve():
    tree = generate_tree()
    return sum(min(find_cliques(tree, size=5), key=sum))

if __name__ == "__main__":
    solve()