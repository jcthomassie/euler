from euler.problem_23 import solve

from .utils import validate_solution


def test_solution():
    validate_solution(solve, answer=4179871)
