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

def pair(hand):
   return funcy.has_dups(2)(hand)

def two_pair(hand):
   return hand[0] == hand[1] and hand[2] == hand[3] \
       or hand[0] == hand[1] and hand[3] == hand[4] \
       or hand[1] == hand[2] and hand[3] == hand[4]

def three_of_a_kind(hand):
   return funcy.has_dups(3)(hand)

def straight(hand):
   is_straight = True
   for i in range(util.HAND_SIZE - 1):
      is_straight = is_straight and hand[i + 1].is_after(hand[i])
   return is_straight

def flush(hand):
   return len(list(filter(
      lambda card: card.suit is hand[0].suit, hand))) == util.HAND_SIZE

def full_house(hand):
   return hand[0] == hand[1] and hand[1] == hand[2] and hand[3] == hand[4] \
       or hand[0] == hand[1] and hand[2] == hand[3] and hand[3] == hand[4]

def four_of_a_kind(hand):
   return funcy.has_dups(4)(hand)

def straight_flush(hand):
   return straight(hand) and flush(hand)

def royal_flush(hand):
   return straight_flush(hand) and hand[-1].value() == len(util.RANKS) - 1

def get_score(hand):
   if royal_flush(hand):
      score = 9
   elif straight_flush(hand):
      score = 8
   elif four_of_a_kind(hand):
      score = 7
   elif full_house(hand):
      score = 6
   elif flush(hand):
      score = 5
   elif straight(hand):
      score = 4
   elif three_of_a_kind(hand):
      score = 3
   elif two_pair(hand):
      score = 2
   elif pair(hand):
      score = 1
   else:
      score = 0
   return score

def showdown(player_hand, comp_hand):
   player_score = get_score(player_hand)
   comp_score = get_score(comp_hand)
   winning_hand = util.HANDS[max(player_score, comp_score)]
   winner = "Player" if player_score > comp_score else "Computer"
   return winner, winning_hand

def play():
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
   player_hand = funcy.remove_at(player_hand, muck)
   player_hand += deal(deck, len(muck))
   player_hand.sort()
   io.endgame(player_hand, comp_hand, *showdown(player_hand, comp_hand))
