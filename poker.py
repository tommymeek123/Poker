#!/usr/bin/env python3

"""
poker.py

This module contains functions that model game logic for the Poker project.
"""

__author__ = "Tommy Meek"
__version__ = "(April, 2020)"

import card
import game_io
import random


def make_deck():
   suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
   ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", \
            "Ten", "Jack", "Queen", "King", "Ace"]
   deck = []
   for s in suits:
      for r in ranks:
         deck.append(card.Card(r, s))
   return deck

def shuffle(deck):
   for i in range(len(deck) - 1, 0, -1):
      j = random.randint(0, i)
      deck[i], deck[j] = deck[j], deck[i]
   return deck

def deal(deck, num_cards):
   cards = []
   for i in range(num_cards):
      cards.append(deck.pop())
   return cards

def go():
   HAND_SIZE = 5
   deck = shuffle(make_deck())
   comp_hand = deal(deck, HAND_SIZE)
   player_hand = deal(deck, HAND_SIZE)
   # sort (maybe)
   game_io.display(player_hand)
   muck = game_io.discard()
   # showdown
   game_io.endgame(player_hand, comp_hand, "Player", "Hand")
