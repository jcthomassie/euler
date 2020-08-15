import pytest

problem = pytest.importorskip("euler.problem_34")


def test_solution(validate_solution):
    validate_solution(problem, answer=40730)
