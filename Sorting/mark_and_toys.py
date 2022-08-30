#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    sortedPrice = sorted(prices)
    items = 0
    sumCost = 0
    for p in sortedPrice:
        if sumCost + p <= k:
            sumCost+=p
            items+=1
        else:
            return items
    return items    

if __name__ == '__main__':
   

    prices = list(map(int, "3 7 2 9 4".rstrip().split()))

    result = maximumToys(prices, 15)

    print(result)