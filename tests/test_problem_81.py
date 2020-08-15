import pytest

problem = pytest.importorskip("euler.problem_81")


def test_solution(validate_solution):
    validate_solution(problem, answer=427337)
