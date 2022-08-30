#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
      print(node.data)
      node = node.next
        # fptr.write(str(node.data))

        # node = node.next

        # if node:
        #     fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # Write your code here
    
    newNode =   DoublyLinkedListNode(data)  
    if llist == None:
        return node
    
    if data<llist.data:
        newNode.next = llist
        llist.prev = newNode
        return newNode
        
    node = llist
    while data >= node.data and node.next != None:
        node = node.next
  
    if data >= node.data : # we got to the end of the LinkedList
        newNode.prev = node
        node.next = newNode        
        
    else: 
      newNode.prev = node.prev
      node.prev.next = newNode
      newNode.next = node
      node.prev = newNode      
    return llist
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #t = 5 #int(input())

   # for t_itr in range(t):
    llist_count = [2, 3, 4]

    llist = DoublyLinkedList()

    for i in llist_count:
        #llist_item = DoublyLinkedListNode(list[i])
        llist.insert_node(i)

    data = 1

    llist1 = sortedInsert(llist.head, data)
    print_doubly_linked_list(llist1, ' ', None)

        # print_doubly_linked_list(llist1, ' ', fptr)
    #     fptr.write('\n')

    # fptr.close()
