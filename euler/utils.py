"""
Shared utility functions.
"""
import functools
import time
from typing import Callable

import numpy as np
import pyperclip

def print_result(func: Callable, verbose=False) -> Callable:
    """
    Time the function call; print the call syntax, runtime, and result after
    call finishes before returning the result.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        t1 = time.time()
        # Print timing information
        params = args + tuple(f"{k}={v}" for k, v in kwargs.items())
        f_repr = f"{func.__name__}({','.join(params)})"
        print(f"[{f_repr} = {res}] ({t1 - t0:.3f} sec)")
        # Copy result to clipboard
        pyperclip.copy(str(res))
        return res
    return wrapper

def prime_mask(n):
    """
    Generates a boolean array of length N, where each index is True if that
    index is prime.
    """
    primes = np.ones(n, dtype=bool)
    primes[:2] = False
    for i in range(2, n):
        if primes[i]:
            # Mark all multiples of i as composite
            j = 1
            while True:
                j += 1
                composite = i * j
                if composite >= n:
                    break
                primes[composite] = False
    return primes

def prime_list(n):
    """
    Generates a list of all primes below the input number.
    """
    mask = prime_mask(n)
    return [i for i in range(n) if mask[i]]
