#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr = sorted(arr)
    start = 0
    end = k-1
    
    smin_index = 0   
    min_val = arr[end] - arr[start]
    
    while end < len(arr):
        temp_min = arr[end] - arr[start]
        if temp_min < min_val:
            min_val = temp_min
            smin_index = start
        start +=1
        end +=1
    
    return   min_val      
        
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    k = 3

    arr = [10, 100,300,200,1000,20,30]

    # for _ in range(n):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
