from euler.problem_17 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=21124)
