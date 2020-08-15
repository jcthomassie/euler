import pytest

problem = pytest.importorskip("euler.problem_27")


def test_solution(validate_solution):
    validate_solution(problem, answer=-59231)
