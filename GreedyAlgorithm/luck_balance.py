#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    test = sorted(contests, key=lambda x: x[0], reverse=True)
   
    balance = 0
    one_counter = 0
    for (val, flag) in test:
      if flag == 0:
        balance += val
      if flag ==1: 
        if one_counter < k:
            balance += val
            one_counter+=1
        else:
            balance -= val
    return balance    
           
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    contests = [
      [5, 1],
      [2, 1],
      [1, 1],
      [8, 1],
      [10, 0],
      [5, 0]
    ]
    

    # for _ in range(n):
    #     contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(3, contests)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
