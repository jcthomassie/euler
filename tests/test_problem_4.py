from euler.problem_4 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=906609)
