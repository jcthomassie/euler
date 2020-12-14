import pytest

from euler.problem_84 import (
    Square,
    generate_all_weights,
    get_chance_weights,
    get_community_chest_weights,
    get_final_move_weights,
    get_roll_move_weights,
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


@pytest.mark.parametrize("square", Square)
def test_get_roll_move_weights(square: Square):
    weights = get_roll_move_weights(square)
    assert sum(weights.values()) == 1
    assert Square.JAIL in weights


@pytest.mark.parametrize("square", Square)
def test_get_final_move_weights(square: Square):
    weights = get_final_move_weights(square)
    assert sum(weights.values()) == 1
    assert all(w > 0 for w in weights.values())
    assert Square.JAIL in weights
    assert Square.G2J not in weights


def test_generate_all_weights():
    weights = generate_all_weights()
    assert all(sq in weights for sq in Square if sq != Square.G2J)


def test_solution():
    validate_solution(solve, answer=None)
