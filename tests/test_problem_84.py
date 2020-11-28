import pytest

from euler.problem_84 import get_roll_weights, solve

from .utils import validate_solution


@pytest.mark.parametrize("sides", range(1, 9))
def test_roll_weights(sides: int):
    weights = get_roll_weights(sides)
    assert sum(weights.values()) == 1
    assert len(weights) == 2 * sides - 1


def test_solution():
    validate_solution(solve, answer=None)
