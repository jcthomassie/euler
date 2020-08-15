import pytest

problem = pytest.importorskip("euler.problem_45")


def test_solution(validate_solution):
    validate_solution(problem, answer=1533776805)
