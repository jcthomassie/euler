from euler.problem_83 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=425185)
