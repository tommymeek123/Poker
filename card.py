#!/usr/bin/env python3

"""
card.py

This module contains a Card class that models a playing card.
"""

__author__ = "Tommy Meek"
__version__ = "(April, 2020)"


class Card:

   def __init__(self, rank, suit):
      """ Constructor for the Card class"""

      """ This card's face value. """
      self.rank = rank

      """ This card's suit. """
      self.suit = suit

   @property
   def rank(self):
      """ Accessor for the rank property """
      return self.__rank

   @rank.setter
   def rank(self, rank):
      """ Mutator for the rank property """
      self.__rank = rank

   @property
   def suit(self):
      """ Accessor for the suit property """
      return self.__suit

   @suit.setter
   def suit(self, suit):
      """ Mutator for the suit property """
      self.__suit = suit

   def value(self, rank):
      if rank is "Ace":
         value = 14
      elif rank is "King":
         value = 13
      elif rank is "Queen":
         value = 12
      elif rank is "Jack":
         value = 11
      elif rank is "Ten":
         value = 10
      elif rank is "Nine":
         value = 9
      elif rank is "Eight":
         value = 8
      elif rank is "Seven":
         value = 7
      elif rank is "Six":
         value = 6
      elif rank is "Five":
         value = 5
      elif rank is "Four":
         value = 4
      elif rank is "Three":
         value = 3
      elif rank is "Two":
         value = 2
      return value

   def __eq__(self, other):
      """
      'equals' function. Will be invoked when the '==' operator is used. 
      Compares rank.

      :param other: The card being compared to this card.
      :return: True if this card is of equal rank to the other card.
      """
      return self.rank is other.rank

   def __lt__(self, other):
      """
      'Less than' function. Will be invoked when the '<' operator is used. 
      Compares rank.

      :param other: The card being compared to this card.
      :return: True if this card is of lower rank than the other card.
      """
      return value(self.rank) < value(other.rank)

   def __gt__(self, other):
      """
      'Greater than' function. Will be invoked when the '>' operator is used. 
      Compares rank

      :param other: The card being compared to this card.
      :return: True if this card is of higher rank than the other card.
      """
      return value(self.rank) > value(other.rank)

   def __str__(self):
      """
      'String' function. Will return a string representation of this card.

      :return: A string representation of this card.
      """
      return "{:>5} of {}".format(self.rank, self.suit)

   def __repr__(self):
      """
      'Report' function. Will return a string representation of this card.

      :return: A string representation of this card.
      """
      return str(self)
