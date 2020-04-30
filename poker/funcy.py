"""
poker.funcy.py

A library of funtional tools for any python project.
"""

__author__ = "Tommy Meek"
__date__ = "April, 2020"

from functools import reduce
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

def fy_shuffle(items):
   """
   Fischer-Yates shuffle.

   :param items: A list of items to be shuffled.
   :return: The shuffled list.
   """
   for i in range(len(items) - 1, 0, -1):
      j = random.randint(0, i)
      items[i], items[j] = items[j], items[i]
   return items

def has_dups(n):
   """
   Determines if a list has a specified number of duplicate entries. 
   For example, if 4 is passed as a parameter, this function will only return
   true if an element is present at least 4 times in this list. Note: The 
   list does not have to be sorted.

   :param n: The number of duplicate copies we are looking for.
   :return: An inner function that detects a n duplicate entries
   """
   def detect_dups(list):
      """
      Detects whether a list has any elements duplicated n times.

      :param list: A list that is checked for duplicates.
      :return: True if any element is duplicated n times. False otherwise.
      """
      if len(list) < n:
         return False
      elif list[1:].count(list[0]) >= n - 1:
         return True
      else:
         return detect_dups(list[1:])
   return detect_dups

def remove_at(alist, blist):
   return [alist[i] for i in range(len(alist)) if i not in blist]

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
   items = flatten(list(args))
   return sample(items, len(items)) 

def sexytime(list):
   return reduce(lambda x, y: x + y, filter(list))
