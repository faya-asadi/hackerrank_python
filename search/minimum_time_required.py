#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    m = sorted(machines)
    n = len(machines)
    
    slow = m[n-1]
    fast = m[0]
    
    upper = slow * goal // n
    if (slow * goal) % n != 0:
        upper+=1
    lower = fast * goal // n
    if (fast * goal) % n != 0:
        lower+=1
    mid_days = 0    
    while lower<= upper:
        mid_days = (lower +upper)//2
        production = 0
        for time in m:
            production += mid_days//time
        
        if production < goal:
            lower = mid_days+1
        elif production > goal:
            upper = mid_days
        else:
            return mid_days
    return mid_days            
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nGoal = input().split()

    # n = int(nGoal[0])

    # goal = int(nGoal[1])

    # machines = list(map(int, input().rstrip().split()))
    goal =  56
    machines = [63, 2, 26, 59, 16, 55, 99, 21, 98, 65]
    ans = minTime(machines, goal)
    print(ans)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
