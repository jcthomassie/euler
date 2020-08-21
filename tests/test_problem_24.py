from euler.problem_24 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=2783915460)
