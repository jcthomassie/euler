from euler.problem_22 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=871198282)
