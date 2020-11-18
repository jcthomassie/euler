from euler.problem_37 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=748317)
