#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the substrCount function below.
def substrCount(n, s):
    li = []
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            li.append(s[i:j])
            
    dic = Counter(li)
    cntr = 0
    for key, val in dic.items():
        if len(set(key)) == 1:
            cntr += val
        elif len(set(key)) > 2:
            continue
            
        elif len(key)%2 == 0:
            continue
       
        else:
           index = len(key) //2 
           test = key[:index] + key[index+1:]  # => s = s.replace(s[len(s)//2], '')
           if len(set(test)) == 1:
                cntr += val
              
    return cntr          
            


def substrCount_2(n, s):
    # creating all the substrings
      
    counter = 0
    sub_s = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    for st in sub_s:
        if is_special(st):
            counter+=1
    return counter

def is_special(s):
    if(len(s) == 1 or len(set(s)) == 1):
        return True
    if len(s)%2 == 0:
        return False
    s = s.replace(s[len(s)//2], '')
    return True if  len(set(s)) == 1 else False 
                     
        
    
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # s = input()

    result = substrCount(5, "asasd")
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()


