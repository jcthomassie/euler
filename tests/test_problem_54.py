import pytest

from euler.problem_54 import solve

from .utils import validate_solution


@pytest.mark.solved
def test_solution() -> None:
    validate_solution(solve, answer=376)
