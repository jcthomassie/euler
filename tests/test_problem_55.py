import pytest

problem = pytest.importorskip("euler.problem_55")


def test_solution(validate_solution):
    validate_solution(problem, answer=249)
