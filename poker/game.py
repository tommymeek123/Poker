"""
poker.game.py

This module contains functions that model game logic for the Poker project. 
A simple game of 5-Card Stud is played.
"""

__author__ = "Tommy Meek"
__date__ = "April, 2020"

import card
import poker_io as io
import funcy
import util


def make_deck():
   """
   Creates a standard deck of playing cards.

   :return: A list of Card objects.
   """
   return funcy.exec_all(card.Card, util.RANKS, util.SUITS)

def deal(deck, num_cards):
   """
   Removes a given number of cards from the deck and returns them in a list.

   :param deck: A list of all Card objects not yet used in this game.
   :param num_cards: The amount of cards to remove from the top of the deck.
   :return: A list containing the top few cards from the deck
   """
   cards = []
   for i in range(num_cards):
      cards.append(deck.pop())
   return cards

def has_set(size):
   """
   Determines if a hand has a set of cards of the same rank

   :param size: The size of the set we are looking for.
   :return: An inner function that detects a set of the given size.
   """
   def detect_set(hand):
      #code
      return False
   return detect_set

def go():
   """
   Controller for the game. Calls other functions in an appropriate order.
   """
   deck = funcy.shuffle(make_deck())
   comp_hand = deal(deck, util.HAND_SIZE)
   player_hand = deal(deck, util.HAND_SIZE)
   comp_hand.sort()
   player_hand.sort()
   io.display(player_hand)
   muck = io.discard()
   # showdown
   io.endgame(player_hand, comp_hand, "Player", "Hand")
