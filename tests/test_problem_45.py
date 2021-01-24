from euler.problem_45 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=1533776805)
