# -*- coding: utf-8 -*-
"""Shared utility functions."""
import atexit
import functools
import math
import time
import warnings
from pathlib import Path
from typing import Any, Callable, Iterator, TypeVar, Union, cast

import numpy as np
import numpy.typing as npt
import pyperclip

SolutionType = Union[int, str]
Solver = TypeVar("Solver", bound=Callable[..., SolutionType])


def print_result(func: Solver, verbose: bool = False) -> Solver:
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
        if pyperclip.is_available():
            pyperclip.copy(str(res))
        return res

    return cast(Solver, wrapper)


###############################################################################
# PRIMES
###############################################################################
CACHE_DIR = Path(__file__).parent / "cache"
CACHE_IGNORE = CACHE_DIR / ".gitignore"
CACHE_PRIMES = CACHE_DIR / ".primes.npy"
_PRIME_MASK: npt.NDArray[np.bool_] | None = None
_PRIME_MASK_CHANGED = False


def _cache_init() -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    if not CACHE_IGNORE.exists():
        CACHE_IGNORE.write_text("*")


def _cache_read() -> npt.NDArray[np.bool_]:
    if CACHE_PRIMES.exists():
        return cast(npt.NDArray[np.bool_], np.load(CACHE_PRIMES))
    return np.zeros(2, dtype=np.bool_)


@atexit.register
def _cache_write() -> None:
    if _PRIME_MASK_CHANGED and _PRIME_MASK is not None:
        warnings.warn(f"Writing prime cache (n={len(_PRIME_MASK)}, {CACHE_PRIMES})")
        _cache_init()
        np.save(CACHE_PRIMES, _PRIME_MASK)


def prime_mask(n: int) -> np.ndarray:
    """Generate boolean array of length N, where prime indices are True."""
    global _PRIME_MASK, _PRIME_MASK_CHANGED
    if _PRIME_MASK is None:
        _PRIME_MASK = _cache_read()
    if (alloc := n - len(_PRIME_MASK)) > 0:
        warnings.warn(f"Cache miss on prime mask ({n=}, cached={len(_PRIME_MASK)})")
        # Extend prime mask up to N
        _PRIME_MASK = np.pad(_PRIME_MASK, (0, alloc), constant_values=True)
        _PRIME_MASK.flags.writeable = True
        for i in range(2, n):
            if _PRIME_MASK[i]:
                # Mark all multiples of i as composite
                composite = 2 * i
                while composite < n:
                    _PRIME_MASK[composite] = False
                    composite += i

        # Ensure cache remains valid
        _PRIME_MASK_CHANGED = True
        _PRIME_MASK.flags.writeable = False
    return _PRIME_MASK


def prime_list(n: int) -> list[int]:
    """Generate a list of all primes below the input number."""
    mask = prime_mask(n)
    if n <= 2:
        return []
    return [2, *(i for i in range(3, n, 2) if mask[i])]


@functools.lru_cache
def is_prime(n: int) -> bool:
    """Return True if the input is prime."""
    mask = _PRIME_MASK if _PRIME_MASK is not None else _cache_read()
    if n < len(mask):
        return cast(bool, mask[n])
    if n % 2 == 0 or n % 3 == 0:
        return n == 3  # 1 and 2 are guaranteed covered by the mask
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
    m2 = m**2
    n2 = n**2
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
