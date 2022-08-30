#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # Write your code here
  m, n = len(a), len(b)
  dp = [[False]*(m+1) for _ in range(n+1)]
  dp[0][0] = True
  for i in range(n+1):
      for j in range(m+1):
          if i == 0 and j != 0:
              dp[i][j] = a[j-1].islower() and dp[i][j-1]
          elif i != 0 and j != 0:
              # if a[j-1] == b[i-1] :
              #     dp[i][j] = dp[i-1][j-1]
              if a[j-1] == b[i-1] or a[j-1].upper() == b[i-1]:
                  dp[i][j] = dp[i-1][j-1] or dp[i][j-1]
              elif a[j-1].islower() :
                  dp[i][j] = dp[i][j-1]
  return "YES" if dp[n][m] else "NO"         
            
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # for q_itr in range(q):
    # a = input()

    # b = input()
    
    # a = "daBcd"
    # b = "ABC"
    # a = "UMKFW"
    # b = "UMKFW"
    # a="beFgH"
    # b ="EFG"
    # a = "sYOCa"
    # b = "YOCN"
    
    #ababbaAbAB AABABB false
    a = "ababbaAbAB"
    b = "AABABB"

    # # aAbAb ABAB true
    # a = "aAbAb"
    # b = "ABAB"

    # # baaBa BAAA false
    a = "baaBa"
    b = "BAAA"

    # # abAAb AAA true
    a = "abAAb"
    b = "AAA"

    # # babaABbbAb ABAA false
    a = "babaABbbAb"
    b = "ABAA"
    

    result = abbreviation(a, b)
    
    print(result)

        # fptr.write(result + '\n')

    # fptr.close()
