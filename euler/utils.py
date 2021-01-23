# -*- coding: utf-8 -*-
"""Shared utility functions."""
import functools
import math
import time
from typing import Any, Callable, Iterator, Union

import numpy as np
import pyperclip

SolutionType = Union[int, str]


def print_result(func: Callable[..., SolutionType], verbose: bool = False) -> Callable:
    """
    Time the function call; print the call syntax, runtime, and result after
    call finishes before returning the result.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> SolutionType:
        t_0 = time.perf_counter()
        res = func(*args, **kwargs)
        t_1 = time.perf_counter()
        # Print timing information
        params = args + tuple(f"{k}={v}" for k, v in kwargs.items())
        f_repr = f"{func.__module__}.{func.__name__}({','.join(params)})"
        print(f"[{t_1 - t_0:.5f} sec]\t", f_repr, "\t=", res)
        # Copy result to clipboard
        pyperclip.copy(str(res))
        return res

    return wrapper


###############################################################################
# PRIMES
###############################################################################
def prime_mask(n: int) -> np.array:
    """Generate boolean array of length N, where prime indices are True."""
    primes = np.ones(n, dtype=bool)
    primes[:2] = False
    for i in range(2, n):
        if primes[i]:
            # Mark all multiples of i as composite
            composite = 2 * i
            while composite < n:
                primes[composite] = False
                composite += i
    return primes


def prime_list(n: int) -> list[int]:
    """Generate a list of all primes below the input number."""
    mask = prime_mask(n)
    if n <= 2:
        return []
    return [2, *(i for i in range(3, n, 2) if mask[i])]


@functools.lru_cache
def is_prime(n: int) -> bool:
    """Return True if the input is prime."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.floor(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


###############################################################################
# COPRIMES
##############################################################################
def _coprime_children(m: int, n: int, stop: int) -> Iterator[tuple[int, int]]:
    """
    https://en.wikipedia.org/wiki/Coprime_integers#Generating_all_coprime_pairs
    """
    if m <= stop:
        yield (m, n)
        yield from _coprime_children(2 * m - n, m, stop)
        yield from _coprime_children(2 * m + n, m, stop)
        yield from _coprime_children(m + 2 * n, n, stop)


def coprimes_odd_odd(stop: int) -> list[tuple[int, int]]:
    """Generate all odd coprime pairs `(m, n)` where `stop >= m > n`."""
    return list(_coprime_children(3, 1, stop))


def coprimes_odd_even(stop: int) -> list[tuple[int, int]]:
    """Generate all odd, even coprime pairs `(m, n)` where `stop >= m > n`."""
    return list(_coprime_children(2, 1, stop))


def coprimes(stop: int) -> list[tuple[int, int]]:
    """Generate all coprime pairs `(m, n)` where `stop >= m > n`."""
    return [
        *_coprime_children(3, 1, stop),
        *_coprime_children(2, 1, stop),
    ]


###############################################################################
# TRIANGLES
###############################################################################
Triangle = tuple[int, int, int]
TriangleGenerator = Iterator[Triangle]


def euclid(m: int, n: int) -> Triangle:
    """Get a pythagorean triple (a, b, c) computed using Euclid's formula.

    For proper behavior, inputs must satisfy: `m > n >= 1`

    https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
    """
    m2 = m ** 2
    n2 = n ** 2
    return (
        m2 - n2,  # A
        2 * m * n,  # B
        m2 + n2,  # C
    )


def generate_primitive_triples(stop: int) -> TriangleGenerator:
    """
    Generates all primitive pythagorean triples (a, b, c) where c (the hypotenuse)
    does not exceed ``stop``.

    NOTE: stop handling is buggy; there may be extra triples.
    """
    # c <= stop
    # c = m^2 + n^2
    # c > m^2
    m_max = math.ceil(math.sqrt(stop))
    for m, n in _coprime_children(2, 1, m_max):
        yield euclid(m, n)


def generate_triples(stop: int) -> TriangleGenerator:
    """
    Generates all pythagorean triples (a, b, c) where c (the hypotenuse) does
    not exceed ``stop``.
    """
    for primitive in generate_primitive_triples(stop):
        yield primitive
        for i in range(2, stop):
            triple = tuple((i * side for side in primitive))
            if triple[-1] > stop:
                break
            yield triple  # type: ignore
