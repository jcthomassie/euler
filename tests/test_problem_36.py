from euler.problem_36 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=872187)
