from euler.problem_75 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=161667)
