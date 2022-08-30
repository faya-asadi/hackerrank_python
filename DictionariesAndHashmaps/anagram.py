#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import Counter
from math import factorial

def sherlockAndAnagrams(s):
    # Write your code here
    
    substrList = [ sorted(s[i:j]) for i in range(0, len(s)+1) for j in range(i+1, len(s)+1) ]
    test = []
    for t in substrList:
      test.append("".join(t))
    subStrDic = Counter( test )
   
    anagramCount = 0;
    for v in subStrDic.values():
        if v == 2: anagramCount +=1
        if v> 2:
            com = factorial(v) // factorial(2) // factorial(v-2)
            anagramCount += com
            
    return anagramCount
    



result = sherlockAndAnagrams("abba")
print(result)


       