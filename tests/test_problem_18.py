import pytest

problem = pytest.importorskip("euler.problem_18")


def test_solution(validate_solution):
    validate_solution(problem, answer=1074)
