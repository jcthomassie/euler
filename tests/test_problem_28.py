import pytest

problem = pytest.importorskip("euler.problem_28")


def test_solution(validate_solution):
    validate_solution(problem, answer=669171001)
