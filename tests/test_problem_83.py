import pytest

problem = pytest.importorskip("euler.problem_83")


def test_solution(validate_solution):
    validate_solution(problem, answer=425185)
