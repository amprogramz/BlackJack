from enum import Enum
from enum import IntEnum

# Number of decks to play with
NUM_OF_DECKS = 5

# Number of cards to initially deal
NUM_DEAL_CARDS = 2

# Card value definitions – only use BLACKJACK for initial player card count. A 21 is only a Blackjack at th
# beginning of the game. Use BUST to determine if player has a hand larger than 21 during regular play
BLACKJACK = 21
BUST = 22

class PlayerState(IntEnum):
    PLAYING = 0
    HAS_BLACKJACK = 1
    DONE = 2
    LOSS = 3

class PlayerMove(IntEnum):
    STAND = 0
    HIT = 1
    #DOUBLE_DOWN = 2
    #SPLIT = 3

class CardState(Enum):
    DOWN = False
    UP = True

def main():
    pass


if __name__ == “__main__”:
    main()