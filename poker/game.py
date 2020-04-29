"""
poker.game.py

This module contains functions that model game logic for the Poker project.
"""

__author__ = "Tommy Meek"
__date__ = "(April, 2020)"

import card
import poker_io as io
import funcy
import util


def make_deck():
   return funcy.exec_all(card.Card, util.RANKS, util.SUITS)

def deal(deck, num_cards):
   cards = []
   for i in range(num_cards):
      cards.append(deck.pop())
   return cards

def go():
   deck = funcy.shuffle(make_deck())
   comp_hand = deal(deck, util.HAND_SIZE)
   player_hand = deal(deck, util.HAND_SIZE)
   comp_hand.sort()
   player_hand.sort()
   io.display(player_hand)
   muck = io.discard()
   # showdown
   io.endgame(player_hand, comp_hand, "Player", "Hand")
