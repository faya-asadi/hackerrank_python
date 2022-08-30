#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    if len(note) > len (magazine):
        print( "No")
        return
        
    for word in note:
        if word not in magazine:
            print ("No")
            return
        else:
            magazine.remove(word)
    print("Yes")    


magazine = "give me one grand today night"
note = "give one grand today"
checkMagazine(magazine.split(), note.split())






#######################################


def checkMagazineString(magazine, note):
    # Write your code here
    if len(note) > len (magazine):
        print( "No")
        return
        
    for word in note.split():
        if word not in magazine:
            print ("No")
            return
        else:
            magazine = magazine.replace(word, "", 1)
    print("Yes")    


magazine = "give me one grand today night"
note = "give one grand today"
checkMagazineString(magazine, note)


####################################
def checkMagazineHashmap(magazine, note):
     ### Hashmap
    dicMagazine = {word : magazine.count(word) for word in note}
    dicNote = {word: note.count(word) for word in note}
    for key in dicNote.keys():
        if dicMagazine.get(key) < dicNote.get(key):
            print("No")
            return
    print("Yes")    
    
    
magazine = "give me one grand today night"
note = "give one grand today"
checkMagazineHashmap(magazine.split(), note.split())    


###################################
from collections import Counter

def checkMagazineCounter(magazine, note):
  mCounter = Counter(magazine)
  nCounter = Counter(note)
  result = nCounter - mCounter
  print("Yes") if result == {} else print("No")
  
  
magazine = "give me one grand today night give give"
note = "give one grand today one tomorrow"
checkMagazineCounter(magazine.split(), note.split())   