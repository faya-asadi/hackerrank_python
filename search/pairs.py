#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
from collections import Counter
def pairs(k, arr):
    # Write your code here
    count = 0
    dic = Counter(arr)
    for i in arr:
        if i-k in dic.keys():
            count += dic[i] * dic[i-k]
    return count        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    k = 2 #int(first_multiple_input[1])

    arr = [1, 5, 3, 4, 2]

    result = pairs(k, arr)
    
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
