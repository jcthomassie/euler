from euler.problem_42 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=None)
