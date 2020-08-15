import pytest

problem = pytest.importorskip("euler.problem_82")


def test_solution(validate_solution):
    validate_solution(problem, answer=260324)
