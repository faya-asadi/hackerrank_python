#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    maxHolder = [0 for i in range(0, len(arr))]
    maxHolder[0] = max(0, arr[0])
    maxHolder[1] = max(maxHolder[0], arr[1])
    for i in range(2, len(arr)):
        maxHolder[i] = max(maxHolder[i-1], arr[i], arr[i] + maxHolder[i-2])
    return maxHolder[len(arr)-1]    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # arr = list(map(int, input().rstrip().split()))

    arr = [-7, 5, 3, 8, 10]
    res = maxSubsetSum(arr)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()

