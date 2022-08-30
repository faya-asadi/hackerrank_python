#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    dic = Counter(arr)
    tripletCnt = 0   
    
    for i in dic.keys():
        if dic[i*r] != 0 and dic [i*r*r] != 0:
            tripletCnt += (dic[i] * dic[i*r] * dic [i*r*r] )            
    return tripletCnt



ans = countTriplets([1, 5, 5, 25, 125], 5)
print(ans)

    
ans = countTriplets([1, 3, 9, 9, 27, 81], 3)
print(ans)