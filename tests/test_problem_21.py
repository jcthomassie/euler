import pytest

problem = pytest.importorskip("euler.problem_21")


def test_solution(validate_solution):
    validate_solution(problem, answer=31626)
