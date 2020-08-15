import pytest

problem = pytest.importorskip("euler.problem_1")


def test_solution(validate_solution):
    validate_solution(problem, answer=233168)
