import pytest

problem = pytest.importorskip("euler.problem_44")


def test_solution(validate_solution):
    validate_solution(problem, answer=5482660)
