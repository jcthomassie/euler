from euler.problem_28 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=669171001)
