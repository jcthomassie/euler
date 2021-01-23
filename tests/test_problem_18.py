from euler.problem_18 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=1074)
