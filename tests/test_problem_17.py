import warnings

import pytest

problem = pytest.importorskip("euler.problem_17")

SOLUTION = 21124


def test_solution():
    # Compute solution
    try:
        solution = problem.solve()
    except NotImplementedError:
        warnings.warn("Solution is not yet implemented")
        return
    # Validate solution
    if SOLUTION is None:
        warnings.warn("Correct solution is unknown")
        return
    assert solution == SOLUTION
