"""
@author Tommy Meek
@date April, 2020

poker.game.py
This module contains functions that model game logic for the Poker project. 
A simple game of 5 Card Draw is played.
"""

import card
import poker_io as io
import funcy
import util


def make_deck():
   """ Creates a standard deck of playing cards.

   Returns:
      A list of Card objects.
   """
   return funcy.exec_all(card.Card, util.RANKS, util.SUITS)

def deal(deck, num_cards):
   """ Removes a given number of cards from the deck and returns them in a list.

   Args:
      A list of all Card objects not yet used in this game.
      num_cards: The amount of cards to remove from the top of the deck.

   Returns:
      A list containing the top few cards from the deck
   """
   cards = []
   for i in range(num_cards):
      cards.append(deck.pop())
   return cards

def pair(hand):
   """ Detects a pair.

   Args:
      hand: The hand of cards being considered.

   Returns:
      True if this hand contains a pair. False otherwise.
   """
   return funcy.has_dups(2)(hand)

def two_pair(hand):
   """ Detects a two pair.

   Args:
      hand: The hand of cards being considered.

   Returns:
      True if this hand contains a two pair. False otherwise.
   """
   return funcy.dup_counts(card.Card.rank, hand).count(2) == 2

def three_of_a_kind(hand):
   """ Detects a three of a kind.

   Args:
      hand: The hand of cards being considered.

   Returns:
      True if this hand contains a three of a kind. False otherwise.
   """
   return funcy.has_dups(3)(hand)

def straight(hand):
   """ Detects a straight.

   Args:
      hand: The hand of cards being considered..

   Returns:
      True if this hand contains a straight. False otherwise.
   """
   is_straight = True
   for i in range(util.HAND_SIZE - 1):
      is_straight = is_straight and hand[i + 1].is_after(hand[i])
   return is_straight

def flush(hand):
   """ Detects a flush.

   Args:
      hand: The hand of cards being considered.

   Returns:
      True if this hand contains a flush. False otherwise.
   """
   return len(funcy.prop_match(card.Card.suit, hand[0], hand)) == util.HAND_SIZE

def full_house(hand):
   """ Detects a full house.

   Args:
      hand: The hand of cards being considered.

   Returns:
      True if this hand contains a full house. False otherwise.
   """
   matches = funcy.dup_counts(card.Card.rank, hand)
   return 2 in matches and 3 in matches

def four_of_a_kind(hand):
   """ Detects a four of a kind.

   Args:
      hand: The hand of cards being considered.

   Returns:
      True if this hand contains a four of a kind. False otherwise.
   """
   return funcy.has_dups(4)(hand)

def straight_flush(hand):
   """ Detects a straight flush.

   Args:
      hand: The hand of cards being considered.

   Returns:
      True if this hand contains a straight flush. False otherwise.
   """
   return straight(hand) and flush(hand)

def royal_flush(hand):
   """ Detects a royal flush.

   Args:
      hand: The hand of cards being considered.

   Returns:
      True if this hand contains a royal flush. False otherwise.
   """
   return straight_flush(hand) and hand[-2].value() == len(util.RANKS) - 2

def get_score(hand):
   """ Generates an integer corresponding to a hand's relative value in poker.

   Args:
      hand: The hand of cards being considered.

   Returns:
      A number. A high number means a good hand. A low number means a bad hand.
   """
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

def tiebreak(player_hand, comp_hand):
   """ Decides the winner of a hand if both hands have the same type.

   This is accomplished by determining the hand with the highest high card. 
   This is not in accordance with the standard rules of 5 Card Draw. This is 
   due to the limited scope of this project. This function would need to be 
   more robust to accuratelyt model 5 Card Draw.

   Args:
      player_hand: The player's hand.
      comp_hand: The computer's hand.

   Returns:
      A string representing the winner of the hand.
   """
   if player_hand == [] or comp_hand == []:
      return "Player"
   if player_hand[-1] == comp_hand[-1]:
      return tiebreak(player_hand[:-1], comp_hand[:-1])
   else:
      return "Player" if player_hand[-1] > comp_hand[-1] else "Computer"

def showdown(player_hand, comp_hand):
   """ Determines the winner of the current poker hand.

   Args:
      player_hand: The player's hand.
      comp_hand: The computer's hand.

   Returns:
      A string representing the winner of the hand.
   """
   player_score = get_score(player_hand)
   comp_score = get_score(comp_hand)
   winning_hand = util.HANDS[max(player_score, comp_score)]
   if player_score > comp_score:
      winner = "Player"
   elif player_score < comp_score:
      winner = "Computer"
   else:
      winner = tiebreak(player_hand, comp_hand)
   return winner, winning_hand

def play():
   """ Controller for the game. Calls functions in an appropriate order. """
   deck = funcy.fy_shuffle(make_deck())
   comp_hand = deal(deck, util.HAND_SIZE)
   player_hand = deal(deck, util.HAND_SIZE)
   comp_hand.sort()
   player_hand.sort()
   io.display(player_hand)
   muck = io.discard()
   player_hand= [player_hand[i] for i in range(util.HAND_SIZE) if i not in muck]
   player_hand += deal(deck, len(muck))
   player_hand.sort()
   io.endgame(player_hand, comp_hand, *showdown(player_hand, comp_hand))
