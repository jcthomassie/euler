from euler.problem_1 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=233168)
