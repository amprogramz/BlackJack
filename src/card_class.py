import random
from enum import Enum
class Deck ():
    def __init__(self):
        suites=["hearts","clubs","spades","diamonds"]
        values=["ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.deck_list=[]
        for i in suites:
            for n in values:
                self.deck_list.append((i,n))
    def get_card(self):
        num=random.randrange(0,51)
        print(self.deck_list[num])

test=Deck()
test.get_card()
