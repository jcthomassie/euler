from euler.problem_41 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=7652413)
