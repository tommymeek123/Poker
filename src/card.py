"""
@author Tommy Meek
@date April, 2020

poker.card.py
This module contains a Card class that models a playing card.
"""

import util


class Card:
   """ A standard playing card. 
   
   Attributes:
      rank: This card's face value.
      suit: This card's suit.
   """

   def __init__(self, rank, suit):
      """ Constructor for the Card class. 
   
      Args:
         The rank of this card.
         The suit of this card.
      """
      self.rank = rank
      self.suit = suit

   @property
   def rank(self):
      """ Accessor for the rank property. 
   
      Returns:
         The rank of this card.
      """
      return self.__rank

   @rank.setter
   def rank(self, rank):
      """ Mutator for the rank property. 
   
      Args:
         The rank of this card.
      """
      self.__rank = rank

   @property
   def suit(self):
      """ Accessor for the suit property. 
   
      Returns:
         The suit of this card.
      """
      return self.__suit

   @suit.setter
   def suit(self, suit):
      """ Mutator for the suit property. 
   
      Args:
         The suit of this card.
      """
      self.__suit = suit

   def value(self):
      """ Determines the relative value of this card.

      Returns: 
         The relative value of this card.
      """
      return util.RANKS.index(self.rank)

   def is_after(self, other):
      """ Determines if this card's rank is exactly one higher another.

      Args: 
         other: Another card being compared with this card.

      Return: 
         True if the rank is exactly one higher. False otherwise.
      """
      return self.value() - other.value() == 1

   def __eq__(self, other):
      """ 'Equals'. Invoked when the '==' operator is used. Compares rank.

      Args: 
         other: The card being compared to this card.

      Return: 
         True if this card is of equal rank to the other card.
      """
      return self.rank is other.rank

   def __lt__(self, other):
      """ 'Less than'. Invoked when the '<' operator is used. Compares rank.

      Args: 
         other: The card being compared to this card.

      Return: 
         True if this card is of lower rank than the other card.
      """
      return self.value() < other.value()

   def __gt__(self, other):
      """ 'Greater than'. Invoked when the '>' operator is used. Compares rank

      Args: 
         other: The card being compared to this card.

      Return: 
         True if this card is of higher rank than the other card.
      """
      return self.value() > other.value()

   def __str__(self):
      """ 'String'. Will return a string representation of this card.

      Return: 
         A string representation of this card.
      """
      return "{:>5} of {}".format(self.rank, self.suit)

   def __repr__(self):
      """ 'Report'. Will return a string representation of this card.

      Return: 
         A string representation of this card.
      """
      return "{} of {}".format(self.rank, self.suit)
