#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
from collections import Counter

def makeAnagram(a, b):
    # Write your code here
    from collections import Counter
    dicta = Counter(a)
    dictb = Counter(b)
    
    diff1 = dicta - dictb
    diff2 = dictb-dicta
    return sum(diff1.values()) + sum(diff2.values())
    
    # differences = set(dicta.keys()).symmetric_difference(set(dictb.keys()))
    # similars = set(dicta.keys()).intersection(set(dictb.keys()))
    
    # counter = 0
    # for k in differences:
    #     counter += dicta[k]
    #     counter += dictb[k]
        
    # for k in  similars:
    #     counter += abs(dicta[k]-dictb[k])
    # return counter       
    

    
if __name__ == '__main__':
   
    a = "fcrxzwscanmligyxyvym"
    b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
   

    res = makeAnagram(a, b)
    print(res)

    
