##################################################################
#                    Table class
#
# Contains all cards on table as well as bets
# There should be a way to show whose cards and bets are displayed
#
# Author: Bobby Handley, Blake McGill
# Vers: 01
# Rev 00: set up class definition
# Rev 01: added __init__, __str__, gethands, deal method definitions
##################################################################

import random


def get_card(x=1):
    cardset = dict(Ace=(1, 11), Two=2, Three=3, Four=4,
                   Five=5, Six=6, Seven=7, Eight=8, Nine=9,
                   Ten=10, Jack=10, Queen=10, King=10)

    cards = list(cardset.keys())
    for i in range(x):
        return random.choice(cards)

class BlackJackTable:
    def __init__(self, players_list=None):
        """
        stores player list, default to no players
        :param players_list: contains all players
        """
        self.players = players_list  # list of all participating players
        self.table = dict()  # dictionary of players and their hands
        if not self.players:  # if no players, notify user
            print('No players yet. Please add players.')
        else:  # else generate empty hand for everyone
            for player in self.players:  # for each player
                self.table[player] = []  # set empty hand

    def __repr__(self):
        """
        Prints dictionary of players and their hands
        :return: string of all players and their hands
        """
        tb = 'Table:\n'
        for k in self.table:
            tb = tb + f'{k} has {repr(self.table[k])}.\n'
        return tb

    def gethands(self, player=None):
        """
        Returns list of all cards in play, except your own.
        If no player object passed as arg, returns list of all cards.
        :param player: player requesting table passes self (player's class object)
        :return: list of cards
        """

    def deal(self, player):
        """
        Deal card to player (called from Dealer class only)
        :param player: player to be dealt cards to
        :return: card dealt to player
        """
        for key in range(len(self.players)):
            if player == self.players[key]:
                handbuf = self.table[player]
                handbuf.append(get_card())  # TODO: will append with random card from Deck class
                self.table[player] = handbuf
                print(self.table)


table = BlackJackTable(['Jimmy', 'Timmy', 'Larry'])
table.deal('Jimmy')
