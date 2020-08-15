import pytest

problem = pytest.importorskip("euler.problem_22")


def test_solution(validate_solution):
    validate_solution(problem, answer=871198282)
