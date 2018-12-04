#encoding: utf-8

'''
@brief             	AI for playing Black Jack 

@supported versions	2.7.9

@file   	        handley_player.py

@author                 Bobby Handley

@data                   12/03/18

Indent - 3 spaces
'''

from abstract_player import Abstract_Player


########################################################
#		Handley_Player Class
#
# AI used to play Black Jack
#
# Author: Bobby Handley
########################################################

class Handley_Player(Abstract_Player):
   def __init__(self):
      super(Handley_Player,self).__init__("Bobby")

 
   ### Interface for Dealer to get players status 
   ### Input: None
   ### Output: Player move (hit/pass)
   def play(self):
      return


   ### Interface for dealer to get the bet for a new hand 
   ### Input: None
   ### Output: bet - the ammount of money the player is going to bet(0=not playing this round) 
   def get_bet(self):
      # Logic to determine bet
      bet = 10
      return bet  
