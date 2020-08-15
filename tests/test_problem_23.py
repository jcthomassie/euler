import pytest

problem = pytest.importorskip("euler.problem_23")


def test_solution(validate_solution):
    validate_solution(problem, answer=4179871)
