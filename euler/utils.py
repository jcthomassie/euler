# -*- coding: utf-8 -*-
"""
Shared utility functions.
"""
import functools
import time
from typing import Callable, List

import numpy as np
import pyperclip

def print_result(func: Callable, verbose=False) -> Callable:
    """
    Time the function call; print the call syntax, runtime, and result after
    call finishes before returning the result.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
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

def prime_mask(n: int):
    """
    Generates a boolean array of length N, where each index is True if that
    index is prime.
    """
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

def prime_list(n: int) -> List[int]:
    """
    Generates a list of all primes below the input number.
    """
    mask = prime_mask(n)
    if n <= 2:
        return []
    return [2, *(i for i in range(3, n, 2) if mask[i])]

def _coprime_children(m, n, stop):
    # https://en.wikipedia.org/wiki/Coprime_integers#Generating_all_coprime_pairs
    if m <= stop:
        yield (m, n)
        yield from _coprime_children(2 * m - n, m, stop)
        yield from _coprime_children(2 * m + n, m, stop)
        yield from _coprime_children(m + 2 * n, n, stop)

def coprimes_odd_odd(stop: int) -> List[int]:
    """
    Returns list of all coprime pairs (m, n) where ``stop`` >= m > n
    and both m and n are odd.
    """
    return list(_coprime_children(3, 1, stop))

def coprimes_odd_even(stop: int) -> List[int]:
    """
    Returns list of all coprime pairs (m, n) where ``stop`` >= m > n
    and one of each is even and the other is odd.
    """
    return list(_coprime_children(2, 1, stop))

def coprimes(stop: int) -> List[int]:
    """
    Returns list of all coprime pairs (m, n) where ``stop`` >= m > n.
    """
    return [
        *_coprime_children(3, 1, stop),
        *_coprime_children(2, 1, stop),
    ]
