"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head == None:
        return False
    # dic = {}
    # node = head
    # while node:
    #     if node in dic.keys():
    #         return True        
    #     dic[node] = 1
    #     node = node.next
    # return False     
    slow = head
    fast = head.next
    
    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True    
        
        
        
        
        
        
        
        