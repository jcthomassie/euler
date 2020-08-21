import time
import warnings


def validate_solution(solve, answer=None):
    # Compute solution
    try:
        start = time.perf_counter()
        solution = solve()
        dt = time.perf_counter() - start
        if dt >= 60:
            warnings.warn(f"Solution is slow ({dt:.2f} seconds)")
    except NotImplementedError:
        warnings.warn("Solution is not yet implemented")
        return
    # Validate solution
    if answer is None:
        warnings.warn("Correct solution is unknown")
        return
    assert solution == answer
