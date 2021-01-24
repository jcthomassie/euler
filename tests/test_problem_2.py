from euler.problem_2 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=4613732)
