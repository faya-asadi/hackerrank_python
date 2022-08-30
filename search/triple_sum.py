#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))
    
    ai = 0
    bi = 0
    ci = 0
    
    count = 0
    
    while bi< len(b):
        while ai<len(a) and a[ai] <= b[bi]:
            ai +=1
        while ci<len(c) and c[ci] <= b[bi]:
            ci +=1   
        count += ai * ci
        # ai = 0 we don't need to reset these, since they were smaller than b[bi], they are definitely smaller than b[bi+1]
        # ci = 0
        bi+=1
    return count        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # lenaLenbLenc = input().split()

    # lena = int(lenaLenbLenc[0])

    # lenb = int(lenaLenbLenc[1])

    # lenc = int(lenaLenbLenc[2])

    # arra = list(map(int, input().rstrip().split()))

    # arrb = list(map(int, input().rstrip().split()))

    # arrc = list(map(int, input().rstrip().split()))
    
    arra = [1, 3, 5]
    arrb = [2, 3]
    arrc = [1, 2, 3]

    ans = triplets(arra, arrb, arrc)
    print(ans)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
