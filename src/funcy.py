"""
@author Tommy Meek
@date April, 2020

poker.funcy.py
A library of funtional tools for any python project.
"""

from functools import reduce
from itertools import product
import random


def exec_all(action, *args):
   """ Executes the specified function for every combination of arguments.

   Args:
      action: The function to be executed.
      args: A list of lists of arguments to pass.

   Returns:
      A list containing the values returned by each function call.
   """
   return [action(*tup) for tup in product(*args)]

def prop_match(prop, obj, lst):
   """ Filters a list to objects who share a property with a given object.

   Args:
      prop: A property of the objects passed in.
      obj: An object of the same type as the elements of the list.
      lis: A list of objects.

   Returns:
      A list containing objects who share a property with the given object.
   """
   return list(filter(lambda x: prop.fget(x) is prop.fget(obj), lst))

def remove_dups(lst):
   """ Creates a copy of a list with no duplicates.

   This works on lists of mutable objects unlike the set or dict methods.

   Args:
      lst: A list of objects.

   Returns:
      A shallow copy of the list passed in with duplicates removed.
   """
   no_dups = []
   [no_dups.append(x) for x in lst if x not in no_dups]
   return no_dups

def dup_counts(prop, lst):
   """ Creates a list counting duplicates of each type.

   This function groups objects into types based on the supplied property.

   Args:
      prop: A property of the objects passed in.
      lst: A list of objects.

   Returns:
      A list of integers representing the size of partitions in the list.
   """
   return list(map(len, remove_dups([prop_match(prop, x, lst) for x in lst])))

def fy_shuffle(items):
   """ Fischer-Yates shuffle.

   Args:
      items: A list of items to be shuffled.

   Returns:
      The shuffled list.
   """
   for i in range(len(items) - 1, 0, -1):
      j = random.randint(0, i)
      items[i], items[j] = items[j], items[i]
   return items

def has_dups(n):
   """ Determines if a list has a specified number of duplicate entries.

   For example, if 4 is passed as a parameter, this function will only return
   true if an element is present at least 4 times in this list. Note: The
   list does not have to be sorted.

   Args:
      n: The number of duplicate copies we are looking for.

   Returns:
      An inner function that detects a n duplicate entries
   """
   def detect_dups(list):
      """ Detects whether a list has any elements duplicated n times.

      Args:
         list: A list that is checked for duplicates.

      Returns:
         True if any element is duplicated n times. False otherwise.
      """
      if len(list) < n:
         return False
      elif list[1:].count(list[0]) >= n - 1:
         return True
      else:
         return detect_dups(list[1:])
   return detect_dups
