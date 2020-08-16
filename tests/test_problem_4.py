import pytest

problem = pytest.importorskip("euler.problem_4")


def test_solution(validate_solution):
    validate_solution(problem, answer=906609)
