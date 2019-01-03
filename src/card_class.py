import random
from enum import Enum
from typing import NamedTuple

class Card (object):
   """A standard playing card"""
        suites_list=["hearts","clubs","spades","diamonds"]
        value_dict={
	  "ace"  : (1,11),
	  "2"    : 2,
          "3"    : 3,
          "4"    : 4,
          "5"    : 5,
	  "6"    : 6,
          "7"    : 7,
	  "9"    : 9,
	  "10"   : 10,
          "Jack" : 10,
          "Queen": 10,
          "king" : 10, }
  def __init__(self, suit=None, rank=None):
	self.suit=suit
        self.rank=rank

class Deck ():
    def __init__(self):
        self.deck_list=[]
        for i in suites:
            for n in values:
                self.deck_list.append((i,n))
    def get_card(self):
        num=random.randrange(0,51)
        print(self.deck_list[num])

test=Deck()
test.get_card()
