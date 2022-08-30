#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c = sorted(c, reverse=True)
    flow_num = len(c)    
    flow_cnt = 0
    cost = 0
    time = 0
    while flow_cnt < flow_num:
        time+=1
        for i in range(0, k):
            if flow_cnt >= flow_num:
                return cost
            cost += c[flow_cnt] * time
            flow_cnt+=1
    return cost        
    
    
    
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # c = list(map(int, input().rstrip().split()))

    c=[3, 1 , 9, 5 ,7 ]
    k = 3
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)

    # fptr.write(str(minimumCost) + '\n')

    # fptr.close()
