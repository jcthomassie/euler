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
then highestcards in each hand are compared (see example 4 below); if the
highest cards tie then thenext highest cards are compared, and so on.

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
from utils import print_result


class Card:
    # Suit values
    suits = {
        char: val
        for val, char in enumerate("CDHS")
    }
    # Face values
    faces = {
        char: val
        for val, char in enumerate(list("23456789") + list(("10",)) + list("JQKA"))
    }
    __slots__ = ["value", "suit"]

    def __init__(self, value: int, suit: int):
        self.value = value
        self.suit = suit

    @classmethod
    def from_str(cls, string: str):
        cls(
            cls.faces[string[:-1]],
            cls.suits[string[-1]],
        )

@print_result
def solve():
    return

if __name__ == "__main__":
    solve()
