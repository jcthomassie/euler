"""
Poker hands
===========
https://projecteuler.net/problem=54
"""


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

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @classmethod
    def from_str(cls, string):
        cls(
            cls.faces[string[:-1]],
            cls.suits[string[-1]],
        )

def solve():
    return

if __name__ == "__main__":
    solve()
