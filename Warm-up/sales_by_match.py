#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    match = {}
    count = 0
    for s in ar:
        if s in match:
            count+=1
            del match[s]
        else:
            match[s] = s
    return count
  

  
def sockMerchant_2(n, ar):
    from collections import Counter
    match = Counter(ar)
    cnt = 0
    cnt = sum(num//2 for num in match.values() )    
    return cnt  


result = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
print(result)

result = sockMerchant_2(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
print(result)