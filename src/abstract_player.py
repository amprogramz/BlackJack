#encoding: utf-8

'''
@brief             	AI for playing Black Jack 

@supported versions	2.7.9

@file   	        abstract_player.py

@author                 Bobby Handley

@data                   12/03/18

Indent - 3 spaces
'''

import abc

########################################################
#		Abstract_Player Class
#
# Abstract Player class with all functions needed
# needed to play Black Jack
#
# Author: Bobby Handley
########################################################

import abc 


class Abstract_Player(object):
   __metaclass__ = abc.ABCMeta

   ### Constructor for creating new black jack players
   ### Input: name - Name of player being created
   ### Output: None
   def __init__(self, name="N/A"):
      self._player_name = name
      self.__chips = 100         # Private

   @abc.abstractmethod
   def play(self):
      pass

   @abc.abstractmethod
   def get_bet(self):
      pass  

   def get_chip_count(self):
      return self.__chips 

   def set_chip_count(self, bet):
      if self.__chips - bet >= 0:
         self.__chips -= bet

