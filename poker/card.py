"""
poker.card.py

This module contains a Card class that models a playing card.
"""

__author__ = "Tommy Meek"
__date__ = "April, 2020"

import util


class Card:
   """ A standard playing card. """

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

   def value(self):
      """
      Determines the relative value of this card.

      :return: The relative value of this card.
      """
      return util.RANKS.index(self.rank) + 2

   def is_after(self, other):
      """
      Determines if this card's rank is one higher than that of the argument.

      :param other: Another card being compared with this card.
      :return: True if the rank is exactly one higher. False otherwise.
      """
      return self.value() - other.value() == 1

   def __eq__(self, other):
      """
      'Equals'. Invoked when the '==' operator is used. Compares rank.

      :param other: The card being compared to this card.
      :return: True if this card is of equal rank to the other card.
      """
      return self.rank is other.rank

   def __lt__(self, other):
      """
      'Less than'. Invoked when the '<' operator is used. Compares rank.

      :param other: The card being compared to this card.
      :return: True if this card is of lower rank than the other card.
      """
      return self.value() < other.value()

   def __gt__(self, other):
      """
      'Greater than'. Invoked when the '>' operator is used. Compares rank

      :param other: The card being compared to this card.
      :return: True if this card is of higher rank than the other card.
      """
      return self.value() > other.value()

   def __str__(self):
      """
      'String'. Will return a string representation of this card.

      :return: A string representation of this card.
      """
      return "{:>5} of {}".format(self.rank, self.suit)

   def __repr__(self):
      """
      'Report'. Will return a string representation of this card.

      :return: A string representation of this card.
      """
      return "rank: {}. suit: {}.".format(self.rank, self.suit)
