# -*- coding: utf-8 -*-
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
from typing import DefaultDict, Iterator, Set

from .utils import prime_mask, print_result

P_MAX = 100000000


def generate_graph() -> DefaultDict[int, Set[int]]:
    """Build graph of pairs of 'substring' primes in the prime table."""
    mask = prime_mask(P_MAX)
    graph = defaultdict(set)
    concats = set(
        (  # set of possible concatenated primes
            str(n) for n in range(11, P_MAX, 2) if mask[n]
        )
    )
    for c_1 in concats:
        for i in range(1, len(c_1)):
            if "0" in (c_1[0], c_1[i]):
                continue
            # Check reverse order
            c_2 = c_1[i:] + c_1[:i]
            if c_2 not in concats:
                continue
            # Check substring primes
            a = int(c_1[:i])
            b = int(c_1[i:])
            if mask[a] and mask[b]:
                graph[a].add(b)
                graph[b].add(a)
    return graph


def find_cliques(
    graph: DefaultDict[int, Set[int]], size: int = 5
) -> Iterator[Set[int]]:
    """Find all cliques of the specified size in the input graph."""

    def len_neighbors(n: int) -> int:
        return len(graph[n])

    # largest vertex -> smallest vertex
    for node in sorted(graph.keys(), key=len_neighbors, reverse=True):
        clique = set((node,))
        for neighbor in sorted(graph[node], key=len_neighbors, reverse=True):
            if len_neighbors(neighbor) < size:
                break
            if clique.issubset(graph[neighbor]):
                clique.add(neighbor)
                if len(clique) == size:
                    yield clique
                    break


@print_result
def solve() -> int:
    graph = generate_graph()
    return sum(min(find_cliques(graph, size=5), key=sum))


if __name__ == "__main__":
    solve()
