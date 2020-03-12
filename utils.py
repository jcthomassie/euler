"""
Shared utility functions.
"""
import functools
import time
from typing import Callable

def print_result(func: Callable) -> Callable:
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
        return res
    return wrapper
