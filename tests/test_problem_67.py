from euler.problem_67 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=7273)
