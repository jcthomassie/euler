import pytest

problem = pytest.importorskip("euler.problem_60")


def test_solution(validate_solution):
    validate_solution(problem, answer=26033)
