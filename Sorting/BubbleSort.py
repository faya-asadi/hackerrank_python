#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    countSwap = 0
    checkCount = 0
    # Write your code here
    for i in range(0, len(a)):
        for j in range(0, len(a)-i-1):
            checkCount +=1
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                countSwap +=1
    print("Array is sorted in {} swaps.".format(countSwap))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]) )       
    print("check count: {}".format(checkCount))     

if __name__ == '__main__':
    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))

    countSwaps([4, 2, 3, 1])
    #countSwaps([ 1, 2, 3])
