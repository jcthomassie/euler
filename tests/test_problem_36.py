import pytest

problem = pytest.importorskip("euler.problem_36")


def test_solution(validate_solution):
    validate_solution(problem, answer=872187)
