# -*- coding: utf-8 -*-
"""
Monopoly odds
=============
https://projecteuler.net/problem=84

In the game, Monopoly, the standard board is set up in the following way:

    GO  A1  CC1  A2  T1  R1  B1  CH1  B2  B3  JAIL

    H2                                        C1

    T2                                        U1

    H1                                        C2

    CH3                                       C3

    R4                                        R2

    G3                                        D1

    CC3                                       CC2

    G2                                        D2

    G1                                        D3

    G2J  F3  U2  F2  F1  R3  E3  E2  CH2  E1  FP

A player starts on the GO square and adds the scores on two 6-sided dice to
determine the number of squares they advance in a clockwise direction. Without
any further rules we would expect to visit each square with equal probability:
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH
(chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player
to go directly to jail, if a player rolls three consecutive doubles, they do not
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we are
only concerned with cards that order a movement; any instruction not concerned
with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
    - Advance to GO
    - Go to JAIL

Chance (10/16 cards):
    - Advance to GO
    - Go to JAIL
    - Go to C1
    - Go to E3
    - Go to H2
    - Go to R1
    - Go to next R (railway company)
    - Go to next R
    - Go to next U (utility company)
    - Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll. For
this reason it should be clear that, with the exception of G2J for which the
probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the final
square that the player finishes at on each roll that we are interested in. We
shall make no distinction between "Just Visiting" and being sent to JAIL, and we
shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with sets
of squares.

Statistically it can be shown that the three most popular squares, in order, are
JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So
these three most popular squares can be listed with the six-digit modal string:
102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-
digit modal string.
"""
import enum
from collections import defaultdict
from itertools import combinations_with_replacement
from typing import DefaultDict, Dict

from .utils import print_result


###############################################################################
# SQUARE/BOARD DEFINITIONS -------------------------------------------------- #
###############################################################################
class Square(enum.IntEnum):
    # fmt: off
    [
        GO, A1, CC1, A2, T1, R1, B1, CH1, B2, B3,
        JAIL, C1, U1, C2, C3, R2, D1, CC2, D2, D3,
        FP, E1, CH2, E2, E3, R3, F1, F2, U2, F3,
        G2J, G1, G2, CC3, G3, R4, CH3, H1, T2, H2,
    ] = range(40)
    # fmt: on

    @property
    def group(self) -> str:
        return self.name.strip("1234")

    def move(self, spaces: int) -> "Square":
        """Move from start_sq by spaces."""
        return BOARD[(self + spaces) % len(BOARD)]

    def find_next(self, group: str) -> "Square":
        """Find the next instance of the specified group moving forward (clockwise)."""
        delta = (BOARD_TYPES[self:] + BOARD_TYPES[:self]).index(group)
        return self.move(delta)


# List of all squares in order
# fmt: off
BOARD = (
    GO, A1, CC1, A2, T1, R1, B1, CH1, B2, B3,
    JAIL, C1, U1, C2, C3, R2, D1, CC2, D2, D3,
    FP, E1, CH2, E2, E3, R3, F1, F2, U2, F3,
    G2J, G1, G2, CC3, G3, R4, CH3, H1, T2, H2,
) = list(Square)
# fmt: on


# List of square types in order
BOARD_TYPES = [sq.group for sq in BOARD]


###############################################################################
# PROBABILITIES ------------------------------------------------------------- #
###############################################################################
def _get_roll_weights(sides: int = 6) -> DefaultDict[int, float]:
    weights: DefaultDict[int, float] = defaultdict(lambda: 0)
    rolls = list(combinations_with_replacement(range(1, sides + 1), 2))
    p_roll = 1 / len(rolls)
    for roll in rolls:
        spaces = sum(roll)
        weights[spaces] += p_roll
    return weights


def _get_chance_weights(ch_sq: Square) -> Dict[int, float]:
    cards = 16
    direct = [GO, JAIL, C1, E3, H2, R1]
    return dict(
        (
            (ch_sq.find_next("R"), 2 / cards),  # next railroad (x 2)
            (ch_sq.find_next("U"), 1 / cards),  # next utility
            (ch_sq.move(-3), 1 / cards),  # back 3 spaces
            *((sq, 1 / cards) for sq in direct),  # direct to square
        )
    )


def _get_community_chest_weights() -> Dict[int, float]:
    cards = 16
    direct = [GO, JAIL]
    return dict((sq, 1 / cards) for sq in direct)


ROLL_WEIGHTS = _get_roll_weights()


def _get_move_weights(sq: Square, sides: int = 6) -> DefaultDict[int, float]:
    weights: DefaultDict[int, float] = defaultdict(lambda: 0)
    weights[JAIL] = p_j = (1 / sides) ** 3
    for spaces, weight in ROLL_WEIGHTS.items():
        # Handle doubles
        if spaces % 2 == 0:
            weight -= p_j / sides
        weights[sq.move(spaces)] += weight
    return weights


def generate_all_weights() -> Dict[int, Dict[int, float]]:
    weights: Dict[int, Dict[int, float]] = dict()
    for sq in BOARD:
        w_sq = weights[sq] = dict()
        if sq is G2J:
            w_sq[JAIL] = 1
        elif sq.group in ("CC", "CH"):
            if sq.group == "CH":
                draws = _get_chance_weights(sq)
            else:
                draws = _get_community_chest_weights()
            rolls = _get_move_weights(sq)
            p_roll = 1 - sum(draws.values())  # type: ignore
            for t_sq in set((*draws.keys(), *rolls.keys())):
                w_sq[t_sq] = draws.get(t_sq, 0)
                w_sq[t_sq] += rolls.get(t_sq, 0) * p_roll
        else:
            w_sq.update(_get_move_weights(sq))
    return weights


def print_prob(w: Dict[int, float]) -> None:
    for sq, p in sorted(w.items(), key=lambda t: t[-1]):
        print(sq, f"\t{p * 100:6.3f}%")
    print("TOTAL", f"\t{sum(w.values()) * 100:6.3f}%")


@print_result
def solve() -> str:
    w = generate_all_weights()
    print_prob(w[G1])
    raise NotImplementedError()


if __name__ == "__main__":
    solve()
