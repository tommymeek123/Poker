"""
@author Tommy Meek
@date April, 2020

poker.poker_io.py
This module handles input and output for the Poker project.
"""

from functools import reduce
import card


def display(hand):
   """ Prints the contents of a single hand to the console.

   Args:
      hand: The hand to be printed.
   """
   for i in range(len(hand)):
      print("{}: {}".format(i + 1, hand[i]))
   print()

def score_comment(hand):
   """ Everyone loves snarky comments at the poker table.

   This function evaluates the composition of a hand of cards and prints
   an (in)appropriate repsonse.

   Args:
      hand: The hand to be judged.
   """
   values = list(map(card.Card.value, hand))
   score = reduce(lambda x, y: x + y, values)
   if score < 30:
      print("Those are some pretty small cards.\n")
   elif score > 45:
      print("Whoa! Big cards!\n")

def discard():
   """ Prompts the user for which cards they would like to discard.

   Returns:
      A list of integers corresponding with the indices of the discards.
   """
   muck = ["a"]
   while any([not d.isdigit() or int(d) > 5 for d in muck]):
      muck = input("Which cards would you like to discard? (1-5): ")
      muck = muck.split()
      if any([not d.isdigit() or int(d) > 5 for d in muck]):
         print("Invalid input. Enter numbers (1-5) separated by spaces.\n")
   return [int(d) - 1 for d in muck]

def endgame(player_hand, comp_hand, winner, hand_type):
   """ Displays both hands, the winner, and the type of hand that won.

   Args:
      player_hand: The player's hand.
      comp_hand: The computer's hand.
      winner: The contestant who won the hand.
      hand_type: The type of hand that won.
   """
   print("Your hand:")
   display(player_hand)
   print("The computer's hand:")
   display(comp_hand)
   print(winner + " wins with a " + hand_type)
