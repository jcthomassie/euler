import pytest

problem = pytest.importorskip("euler.problem_24")


def test_solution(validate_solution):
    validate_solution(problem, answer=2783915460)
