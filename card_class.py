import random

class Card():
    def __init__(self, suit, value, face_value):
        self.suit = suit
        self.value = value
        self.face_value = face_value

    def display_card(self):
        print("{0:>2} of {1}".format(self.face_value, self.suit))

class Deck ():
    def __init__(self, num_decks=1):
        self.deck_count = num_decks
        self.count=0
        self.suites_list = ["Hearts", "Clubs", "Spades", "Diamonds"]
        self.value_dict = {
            "A":11,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10}
        self.deck_list=[]
        for deck in range(num_decks):
            self.deck_list.extend(self.__get_deck())
        random.shuffle(self.deck_list)

    def __get_deck(self):
        new_deck = []
        for i in self.suites_list:
            for n in self.value_dict:
                new_deck.append(Card(i,self.value_dict[n],n))
        random.shuffle(new_deck)
        return new_deck

    def reset_deck(self):
        self.deck_list=[]
        for deck in range(self.deck_count):
            self.deck_list.extend(self.__get_deck())
        random.shuffle(self.deck_list)

    def get_card(self):
        new_card = None
        try:
            new_card = self.deck_list.pop()
        except IndexError:
            print("Out of Cards!\nCreating A New Deck")
            self.reset_deck()
            new_card = self.deck_list.pop()
        return new_card



test= Deck()
for x in range(53):
    card=test.get_card()
    card.display_card()
