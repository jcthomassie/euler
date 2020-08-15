import pytest

problem = pytest.importorskip("euler.problem_31")


def test_solution(validate_solution):
    validate_solution(problem, answer=73682)
