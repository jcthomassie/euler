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
from collections import Counter
from utils import print_result


class Card:
    """
    Playing card representation. Allows ordering operations between cards, and
    instantiation from a string representation.
    """
    # Suit values
    suits = {
        char: val
        for val, char in enumerate("CDHS")
    }
    suits_inv = {
        val: char
        for char, val in suits.items()
    }
    # Face values
    faces = {
        char: val
        for val, char in enumerate("23456789TJQKA")
    }
    faces_inv = {
        val: char
        for char, val in faces.items()
    }
    __slots__ = ("face_value", "suit_value")

    def __init__(self, face_value: int, suit_value: int):
        self.face_value = face_value
        self.suit_value = suit_value

    def __eq__(self, other):
        return (
            self.face_value == other.face_value and
            self.suit_value == other.suit_value
        )

    def __gt__(self, other):
        return (
            self.face_value > other.face_value or
            self.face_value == other.face_value and
            self.suit_value > other.suit_value
        )

    def __lt__(self, other):
        return (
            self.face_value < other.face_value or
            self.face_value == other.face_value and
            self.suit_value < other.suit_value
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({self.face_value}, {self.suit_value})"
        )

    def __str__(self) -> str:
        return (
            f"{self.faces_inv[self.face_value]}"
            f"{self.suits_inv[self.suit_value]}"
        )

    @classmethod
    def from_str(cls, string: str):
        return cls(
            cls.faces[string[0]],
            cls.suits[string[-1]],
        )


class Hand:
    """
    Poker hand representation. Contains a list of 5 Card objects. Allows
    ordering operations between hands.
    """
    #__slots__ = ("cards", "_face_counts", "_suit_counts")

    def __init__(self, *cards):
        self.cards = cards
        self._face_counts = Counter()
        self._suit_counts = Counter()
        self._max = None

    @property
    def face_counts(self):
        if not self._face_counts:
            self._face_counts.update(
                c.face_value for c in self.cards
            )
        return self._face_counts

    @property
    def suit_counts(self):
        if not self._suit_counts:
            self._suit_counts.update(
                c.suit_value for c in self.cards
            )
        return self._suit_counts

    def max(self):
        if self._max is None:
            self._max = max(self.cards)
        return self._max

    def is_pair(self):
        return len(self.face_counts) < len(self.cards)

    def is_two_pair(self):
        return False

    def is_three_of_a_kind(self):
        return max()

    def is_straight(self):
        faces = sorted(c.face_value for c in self.cards)
        for a, b in zip(faces, faces[1:]):
            if b != (a + 1):
                return False
        return True

    def is_flush(self):
        suits = set(c.suit_value for c in self.cards)
        return len(suits) == 1

    def is_full_house(self):
        return False

    def is_four_of_a_kind(self):
        return False

    def is_straight_flush(self):
        return (
            self.is_straight() and
            self.is_flush()
        )

    def is_royal_flush(self):
        return (
            self.is_straight_flush() and
            all(c.face_value >= Card.faces["T"] for c in self.cards)
        )

    def __gt__(self, other):
        return self.max() > other.max()

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({' '.join(str(c) for c in self.cards)})"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({', '.join(repr(c) for c in self.cards)})"
        )


def scrape_data(path: str="data/p054_poker.txt"):
    """
    Scrape card data from text file and load it into two Hands, one line at a
    time. Yields Hand pairs.
    """
    with open(path, "r") as h:
        for line in h:
            cards = [
                Card.from_str(card_str)
                for card_str in line.strip().split()
            ]
            yield Hand(*cards[:5]), Hand(*cards[5:])

@print_result
def solve():
    scores = [0, 0]
    for p1_hand, p2_hand in scrape_data():
        scores[p2_hand > p1_hand] += 1
    return scores[0]

if __name__ == "__main__":
    solve()
