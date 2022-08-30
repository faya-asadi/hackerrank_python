#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    index = 0
    jumps = 0
    while(index < len(c)-1):
        index = index+2 if (index+2 < len(c) and c[index+2] == 0) else index+1
        jumps+=1
    return jumps     
  


result = jumpingOnClouds([0,0,1,0,0,1,0])
print(result)

    