#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    #counting the number of as in s
    acount = s.count("a")
    #how many times the whole sentence is repeated
    snumber = n//len(s)
    mod = n % len(s)
    
    return snumber * acount + s[:mod].count("a")


result = repeatedString("abcac", 10)
print(result)
   