#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    c = [1 for i in range(len(arr)) ]
       
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            c[i] = c[i-1]+1
        else:
            c[i] = 1    
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i-1] and c[i-1] <= c[i]:
            c[i-1] = c[i]+1
                 
    return sum(c)        
            
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    arr = [2,4,2,6,1,7,8,9,2,1]

    # for _ in range(n):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)

    result = candies(10, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
