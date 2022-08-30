#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    small = s1 if len(s1) < len(s2) else s2
    big = s2 if small == s1 else s1
    for c in small:
        if c in big:
            return "YES"
        
    return "NO"        


print ( twoStrings("hello", "world").lower() )
print ( twoStrings("hi", "world").upper() )

       