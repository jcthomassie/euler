import pytest

problem = pytest.importorskip("euler.problem_67")


def test_solution(validate_solution):
    validate_solution(problem, answer=7273)
