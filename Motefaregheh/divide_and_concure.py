
import math
import os
import random
import re
import sys

def search_DAC_rec (ary, item):  
  return dac(ary, item, 0, len(ary)-1, 0)

def dac(ary, item, low, high, counter):
  counter+= 1
  print(counter)
  if low > high:
    return -1
  mid_index = (high+low)//2
  mid = ary[mid_index]
  if mid > item:
    #search in the lower half
    return dac(ary, item, low, mid_index-1, counter)
  if mid < item:
    #search in the highr half
    return dac(ary, item, mid_index+1, high, counter)
  return mid_index


def search_DAC_rec_loop (ary, item):  
  low = 0
  high = len(ary) - 1
  counter = 0
  while(low <= high):
    counter+=1
    print(counter)
    mid_index = (low+high)//2
    mid = ary[mid_index]
    if mid > item:
      high = mid_index - 1
    elif mid < item:
        low = mid_index + 1
    else:
      return mid_index
  return -1      



sorted_ary = [1, 2, 3, 4, 5, 6, 7,8, 9]
print(f"result is: {search_DAC_rec(sorted_ary, 9)}")

print(f"result is: {search_DAC_rec_loop(sorted_ary, 1)}")

