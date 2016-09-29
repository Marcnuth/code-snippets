# coding: utf-8
from tree import BTree, BNode

# This method will generate a invert binary tree corresponding to original one
# And won't change any node on the old one
def invert(tree):
    return BTree(__invert(tree.root))

def __invert(node):
    if node is None:
        return None

    if node.left is None and node.right is None:
        return node
    
    left = __invert(node.left)
    right = __invert(node.right)
    return BNode(node.data, right, left)




        
