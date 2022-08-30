""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    check_node(root, -1, 100000)
    
def check_node(root, min_val, max_val):     
    if root == None:
        return True
    if root.data <= min_val or root.data >= max_val:
        return False
    return check_node(root.left, min_val, root.data) and check_node(root.right, root.data, max_val)



