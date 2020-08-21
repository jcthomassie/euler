from euler.problem_31 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=73682)
