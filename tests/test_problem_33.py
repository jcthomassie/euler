from euler.problem_33 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=100)
