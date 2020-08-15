import warnings

import pytest

problem = pytest.importorskip("euler.problem_36")

SOLUTION = 872187


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
