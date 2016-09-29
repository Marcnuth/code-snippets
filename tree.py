# coding: utf-8

class BNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self, root):
        self.root = root
