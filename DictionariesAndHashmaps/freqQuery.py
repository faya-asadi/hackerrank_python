#!/bin/python3

import math
import os
import random
import re
import sys


from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    holder = defaultdict(int)
    ary = []
    for (x,y) in queries:
        if x == 1:
            holder[y] = 1 if holder[y] == 0 else holder[y]+ 1
        elif x == 2:
            if holder[y]>0: holder[y]-=1
        elif x==3 :
            if y in holder.values():
                ary.append(1)
            else:
                ary.append(0)
    return ary            
                



ans = freqQuery([
[1, 3],
[2, 3],
[3, 2],
[1, 4],
[1, 5],
[1, 5],
[1, 4],
[3, 2],
[2, 4],
[3, 2] 
])
print(ans)




# Complete the freqQuery function below.
def freqQueryCounterInPlace(queries):
    holder = defaultdict(int)
    counter = defaultdict(int)
    ary = []
    for (x,y) in queries:
        if x == 1:
            counter[holder[y]]-=1
            holder[y] = 1 if holder[y] == 0 else holder[y]+ 1
            counter[holder[y]]+=1
        elif x == 2:
            counter[holder[y]]-=1
            if holder[y]>0: holder[y]-=1
            counter[holder[y]]+=1
        elif x==3 :
            if counter[y] > 0:
                ary.append(1)
            else:
                ary.append(0)
    return ary            
                
                

ans = freqQueryCounterInPlace([
[1, 3],
[2, 3],
[3, 2],
[1, 4],
[1, 5],
[1, 5],
[1, 4],
[3, 2],
[2, 4],
[3, 2] 
])
print(ans)                