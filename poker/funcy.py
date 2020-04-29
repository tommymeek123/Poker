"""
poker.funcy.py

A library of funtional tools for any python project.
"""

__author__ = "Tommy Meek"
__date__ = "April, 2020"

from itertools import product
from random import sample


def exec_all(action, *args):
   """
   Executes the specified function for every combination of arguments possible.

   :param action: The function to be executed.
   :param args: A list of lists of arguments to pass.
   :return: A list containing the values returned by each function call.
   """
   return [action(*tup) for tup in product(*args)]

def flatten(S):
   """
   Flattens a list of lists recursively.

   :param S: A list of lists.
   :return: A single dimensional list containing all non-list subelements in S.
   """
   if S == []:
      return S
   if isinstance(S[0], list):
      return flatten(S[0]) + flatten(S[1:])
   return S[:1] + flatten(S[1:])

def shuffle(*args):
   """
   Shuffles all base elements in an unspecified number of lists.

   :param args: Any number of items or lists of items to be shuffled.
   :return: A list containing all subelements in random order.
   """
   l = flatten(list(args))
   return sample(l, len(l)) 

# def fy_shuffle(deck):
#    """
#    Fischer-Yates shuffle.

#    :param deck: A deck of objects to be shuffled.
#    :return: The shuffled deck.
#    """
#    for i in range(len(deck) - 1, 0, -1):
#       j = random.randint(0, i)
#       deck[i], deck[j] = deck[j], deck[i]
#    return deck
