import pytest

problem = pytest.importorskip("euler.problem_75")


def test_solution(validate_solution):
    validate_solution(problem, answer=161667)
