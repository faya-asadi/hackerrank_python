
import math
import os
import random
import re
import sys

#Given an array of numbers and a target integer find element pairs that sum up to the target

def find_numbers (ary, target):
  dict = {}
  for n in ary:
    dict[n] = n
  for n in dict.keys():
    other = target-n
    if other in dict.keys():
      return n, other
    
ary = [1, 9, 5, 8, 3, 2]
x, y = find_numbers(ary, 13)    
print(f"x: {x} , y: {y}")