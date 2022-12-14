#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    # current_1 = head1
    # current_2 = head2
    # while(current_1 != current_2):
    #     if current_1.next == None:
    #         current1 = head2
    #     else:
    #         current_1 = current_1.next
    #     if current_2.next == None:
    #         current2 = head1
    #     else:
    #         current_2 = current_2.next 
    # result = []         
    
    # return current_1.data     

    counter1 = 0
    counter2 = 0
    node1 = head1
    node2 = head2
    while node1 != None:
        counter1 +=1
        node1 = node1.next
    while node2 != None:
        counter2 +=1
        node2 = node2.next     

    
    node1 = head1
    node2 = head2    

    diff = abs(counter1 - counter2)
    
    if counter1 > counter2:        
        for i in (0, diff-1):
            node1 = node1.next       
    else :       
        for i in (0, diff-1):
            node2 = node2.next
            
    while(node1 != node2):
        node1 = node1.next
        node2 = node2.next
   
    return node1.data       
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()