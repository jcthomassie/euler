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
from typing import Iterator

from .utils import is_prime, prime_list, print_result


def concats_prime(m: int, n: int) -> bool:
    """Return True if inputs concatenate to a prime."""
    return is_prime(int(f"{m}{n}")) and is_prime(int(f"{n}{m}"))


def generate_graph(node_max: int) -> defaultdict[int, set[int]]:
    """Build graph of pairs of 'substring' primes in the prime table."""
    graph = defaultdict(set)
    primes = prime_list(node_max)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            p = primes[i]
            q = primes[j]
            if concats_prime(p, q):
                graph[p].add(q)
                graph[q].add(p)
    return graph


def find_cliques(
    graph: defaultdict[int, set[int]], size: int = 5
) -> Iterator[set[int]]:
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
    graph = generate_graph(10_000)
    return sum(min(find_cliques(graph, size=5), key=sum))  # type: ignore


if __name__ == "__main__":
    solve()
