# -*- coding: utf-8 -*-
"""
Poker hands
===========
https://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    The cards are valued in the order:
        2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

    Hand	[Player 1]        [Player 2]        [Winner]
    1	 	5H 5C 6S 7S KD    2C 3S 8S 8D TD    Player 2
            Pair: Fives       Pair: Eights

    2	 	5D 8C 9S JS AC    2C 5C 7D 8S QH    Player 1
            High: Ace         High: Queen

    3	 	2D 9C AS AH AC    3D 6D 7D TD QD    Player 2
            Trips: Aces       Flush: Diamonds

    4       4D 6S 9H QH QC    3D 6D 7H QD QS    Player 1
            Pair: Queens      Pair: Queens
            High: Nine        High: Seven

    5	 	2H 2D 4C 4D 4S    3C 3D 3S 9S 9D    Player 1
            Full House        Full House
            w/Three Fours     w/Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator, Optional

from . import DATA_DIR
from .utils import print_result

# Suit values
SUITS = {char: val for val, char in enumerate("CDHS")}
SUITS_INV = {val: char for char, val in SUITS.items()}

# Face values
FACES = {char: val for val, char in enumerate("23456789TJQKA")}
FACES_INV = {val: char for char, val in FACES.items()}


@dataclass(frozen=True, eq=True, repr=True)
class Card:
    """Playing card representation.

    Allows ordering operations between cards, and instantiation from a string
    representation.
    """

    face: int
    suit: int

    def __gt__(self, other: object) -> bool:
        if other is None:
            return True
        if not isinstance(other, Card):
            return NotImplemented
        return (
            self.face > other.face or self.face == other.face and self.suit > other.suit
        )

    def __lt__(self, other: object) -> bool:
        if other is None:
            return False
        if not isinstance(other, Card):
            return NotImplemented
        return (
            self.face < other.face or self.face == other.face and self.suit < other.suit
        )

    def __str__(self) -> str:
        return f"{FACES_INV[self.face]}{SUITS_INV[self.suit]}"

    @classmethod
    def from_str(cls, string: str) -> Card:
        return cls(FACES[string[0]], SUITS[string[-1]])


class Hand:
    """Poker hand representation.

    Contains a list of 5 Card objects. Allows ordering operations between hands.
    """

    _faces_descending = range(len(FACES))[::-1]
    _suits_descending = range(len(SUITS))[::-1]

    __slots__ = ("cards", "_face_counts", "_suit_counts")

    def __init__(self, *cards: Card) -> None:
        # Cards are sorted in descending order; max is always first card
        self.cards = sorted(cards, reverse=True)
        self._face_counts: Optional[Counter[int]] = None
        self._suit_counts: Optional[Counter[int]] = None

    @property
    def face_counts(self) -> Counter[int]:
        if self._face_counts is None:
            self._face_counts = Counter(c.face for c in self.cards)
        return self._face_counts

    @property
    def suit_counts(self) -> Counter[int]:
        if self._suit_counts is None:
            self._suit_counts = Counter(c.suit for c in self.cards)
        return self._suit_counts

    def get_where(
        self, face: Optional[int] = None, suit: Optional[int] = None
    ) -> Iterator[Card]:
        """Get cards that match the input face and suit.

        Yields:
            Matches in descending order.
        """
        for card in self.cards:
            if (face is None or card.face == face) and (
                suit is None or card.suit == suit
            ):
                yield card

    def eval_high(self) -> Card:
        return self.cards[0]

    def eval_pair(self) -> Optional[Card]:
        for face in self._faces_descending:
            if self.face_counts[face] == 2:
                return next(self.get_where(face=face))
        return None

    def eval_two_pair(self) -> Optional[Card]:
        counts = list(self.face_counts.values())
        if counts.count(2) >= 2:
            return self.eval_pair()
        return None

    def eval_three_of_a_kind(self) -> Optional[Card]:
        for face in self._faces_descending:
            if self.face_counts[face] == 3:
                return next(self.get_where(face=face))
        return None

    def eval_straight(self) -> Optional[Card]:
        faces = sorted((c.face for c in self.cards), reverse=True)
        for a, b in zip(faces, faces[1:]):
            if b != (a - 1):
                return None
        return self.cards[0]

    def eval_flush(self) -> Optional[Card]:
        for suit in self._suits_descending:
            if self.suit_counts[suit] == 5:
                return self.cards[0]
        return None

    def eval_full_house(self) -> Optional[Card]:
        counts = self.face_counts.values()
        if 3 in counts and 2 in counts:
            return self.eval_three_of_a_kind()
        return None

    def eval_four_of_a_kind(self) -> Optional[Card]:
        for face in self._faces_descending:
            if self.face_counts[face] == 4:
                return next(self.get_where(face=face))
        return None

    def eval_straight_flush(self) -> Optional[Card]:
        if self.eval_straight() and self.eval_flush():
            return self.cards[0]
        return None

    def eval_royal_flush(self) -> Optional[Card]:
        if self.eval_straight_flush():
            if self.cards[0].face == FACES["A"]:
                return self.cards[0]
        return None

    hierarchy: list[Callable[[Hand], Optional[Card]]] = [
        eval_royal_flush,
        eval_straight_flush,
        eval_four_of_a_kind,
        eval_full_house,
        eval_flush,
        eval_straight,
        eval_three_of_a_kind,
        eval_two_pair,
        eval_pair,
        eval_high,
    ]

    def get_best(self) -> str:
        """Get best card set from hand."""
        for method in self.hierarchy:
            if method(self) is not None:
                return method.__name__.lstrip("eval_")
        raise RuntimeError("Failed to get best card set")

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        for method in self.hierarchy:
            res_s = method(self)
            res_o = method(other)
            if res_s is None:
                if res_o is None:
                    continue
                return False
            if res_s > res_o:
                return True
            if res_s < res_o:
                return False
        return False

    def __bool__(self) -> bool:
        return bool(self.cards)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({' '.join(str(c) for c in self.cards)})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(repr(c) for c in self.cards)})"


def scrape_data(path: Path) -> Iterator[tuple[Hand, Hand]]:
    """Scrape card data from text file and load it into two Hands.

    Yields:
        Pair of hands for one round.
    """
    with path.open() as h:
        for line in h:
            cards = [Card.from_str(card_str) for card_str in line.strip().split()]
            yield Hand(*cards[:5]), Hand(*cards[5:])


@print_result
def solve() -> int:
    scores = [0, 0]
    for p1_hand, p2_hand in scrape_data(DATA_DIR / "p054_poker.txt"):
        if p1_hand > p2_hand:
            scores[0] += 1
        else:
            scores[1] += 1
    return scores[0]


if __name__ == "__main__":
    solve()
