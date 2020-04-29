"""
poker.poker_io.py

This module input and output for the Poker project.
"""

__author__ = "Tommy Meek"
__date__ = "April, 2020"


def display(hand):
   """
   Prints the contents of a single hand to the console.

   :param hand: The hand to be printed.
   """
   for i in range(len(hand)):
      print("{}: {}".format(i + 1, hand[i]))
   print()

def discard():
   """
   Prompts the user for which cards they would like to discard.

   :return: A list of integers corresponding with the indices of the discards.
   """
   muck = input("Which cards would you like to discard? (1-5): ")
   return [int(d) - 1 for d in muck.split()]

def endgame(player_hand, comp_hand, winner, hand_type):
   """
   Prints the contents of both hands to the console then displays the winner 
   along with the type of hand that won.

   :param player_hand: The player's hand.
   :param comp_hand: The computer's hand.
   :param winner: The contestant who won the hand.
   :param hand_type: The type of hand that won.
   """
   print("Your hand:")
   display(player_hand)
   print("The computer's hand:")
   display(comp_hand)
   print(winner + " wins with a " + hand_type)
