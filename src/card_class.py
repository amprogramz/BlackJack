import random
from enum import Enum
from enum import auto

class Deck ():
    def __init__(self):
        self.decklist=[]
        for suit in Card.Suit:
            for n in Card.Value:
                self.decklist.append((suit, n))
    def get_card(self):
        num=random.randrange(0,51)
        print(self.decklist[num])

test=Deck()
test.get_card()

class Card:
    class Suit(Enum):
        HEARTS = auto()
        CLUBS = auto()
        DIAMONDS = auto()
        SPADES = auto()

    class Value(Enum):
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 10
        QUEEN = 10
        KING = 10
        ACE = 11
