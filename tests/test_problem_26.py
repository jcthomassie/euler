import pytest

problem = pytest.importorskip("euler.problem_26")


def test_solution(validate_solution):
    validate_solution(problem, answer=None)
