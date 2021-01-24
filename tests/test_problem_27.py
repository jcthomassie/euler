from euler.problem_27 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=-59231)
