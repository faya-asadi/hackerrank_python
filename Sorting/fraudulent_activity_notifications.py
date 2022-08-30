#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    noticeCount = 0
    for i in range(0, len(expenditure)-d ):
        li = sorted(expenditure[i:i+d])
        med = li[d//2] if d%2 != 0 else (li[d//2] + li[d//2+1])/2
        if expenditure[i+d] >= 2* med:
            noticeCount+=1
    return noticeCount        
        
        
    
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # d = int(first_multiple_input[1])

   # expenditure = list(map(int, input().rstrip().split()))
    expenditure = list(map(int, "10 20 30 40 50".rstrip().split()))
    

    result = activityNotifications(expenditure, 3)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
