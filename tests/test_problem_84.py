import pytest

from euler.problem_84 import (
    Square,
    get_chance_weights,
    get_community_chest_weights,
    get_roll_weights,
    solve,
)

from .utils import validate_solution


@pytest.mark.parametrize("sides", range(1, 9))
def test_get_roll_weights(sides: int):
    weights = get_roll_weights(sides)
    assert sum(weights.values()) == 1
    assert len(weights) == 2 * sides - 1


@pytest.mark.parametrize("square", (Square.CH1, Square.CH2, Square.CH3))
def test_get_chance_roll_weights(square: Square):
    weights = get_chance_weights(square)
    assert sum(weights.values()) == 1
    assert square in weights


@pytest.mark.parametrize("square", (Square.CC1, Square.CC2, Square.CC3))
def test_get_community_chest_roll_weights(square: Square):
    weights = get_community_chest_weights(square)
    assert sum(weights.values()) == 1
    assert square in weights


def test_solution():
    validate_solution(solve, answer=None)
