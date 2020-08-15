import pytest

problem = pytest.importorskip("euler.problem_2")


def test_solution(validate_solution):
    validate_solution(problem, answer=4613732)
