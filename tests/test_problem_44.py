from euler.problem_44 import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=5482660)
