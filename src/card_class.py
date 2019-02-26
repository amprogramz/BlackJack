import random

class Deck ():
    def __init__(self):
        self.count=0
        self.suites_list = ["Hearts", "Clubs", "Spades", "Diamonds"]
        self.value_dict = {
            "ace":11,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "king": 10}

        self.deck_list=[]
        for i in self.suites_list:
            for n in self.value_dict:
                self.deck_list.append((i,n))
                self.count+=1
        print(self.count)

    def get_card(self):
        self.num=random.randrange(0,self.count-1)
        self.card=self.deck_list[self.num]
        print("{1} of {0}".format(self.card[0],self.card[1]))
        self.remove_card(self.card)
        return self.card

    def remove_card(self,card):
        try:
            self.deck_list.remove(card)
            self.count-=1
            print(self.count)
        except ValueError:
            print("Card not found in deck, Could not be removed")
    def display_card(self,card):
        print("{1} of {0}".format(self.card[0], self.card[1]))

