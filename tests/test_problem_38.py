from euler.problem_38 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=932718654)
