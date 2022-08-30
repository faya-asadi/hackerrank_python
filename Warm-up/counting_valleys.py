#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here  
    
    level = 0    
    counter = 0    
    for step in path:
        level= level+1  if step == "U" else level-1      
        if level == 0 and step == "U" :
            counter +=1  
    return counter      


result = countingValleys(8, "UDDDUDUU")
print(result)

   