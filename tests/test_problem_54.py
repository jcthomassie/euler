import pytest

problem = pytest.importorskip("euler.problem_54")


def test_solution(validate_solution):
    validate_solution(problem, answer=376)
