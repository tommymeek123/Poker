"""
@author Tommy Meek
@date April, 2020

poker.util.py
This module contains lists and constants for use in the poker project.
"""

""" All possible ranks of a playing card. """
RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", \
         "Ten", "Jack", "Queen", "King", "Ace"]

""" All possible suits of a playing card. """
SUITS = ["Hearts", "Spades", "Diamonds", "Clubs"]

""" All possible winning hand types in a game of poker. """
HANDS = ["High Card", "Pair", "Two Pair", "Three of a Kind", "Straight", \
         "Flush", "Full House", "Four of a Kind", "Straight Flush", \
         "Royal Flush"]

""" The amount of cards in each poker hand. """
HAND_SIZE = 5
