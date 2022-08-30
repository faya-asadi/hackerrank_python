#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
  # Write your code here
  l = len(s1)
  ary = [[0 for i in range(l+1)] for j in range(l+1)]
  for i in range(1, l+1):
      for j in range(1, l+1):
          if s1[i-1] == s2[j-1]:
              ary[i][j] = ary[i-1][j-1] +1
          else:
              ary[i][j] = max(ary[i-1][j], ary[i][j-1])
  return ary[l][l]    
       
 
 


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s1 = input()

    # s2 = input()
    
    


    result = commonChild("HARRY", "SALLY")
    print(result)
    
    
    result = commonChild("SHINCHAN", "NOHARAAA")
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
