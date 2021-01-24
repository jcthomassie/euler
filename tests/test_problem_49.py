from euler.problem_49 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=296962999629)
