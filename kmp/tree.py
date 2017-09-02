class Node:
    def __init__(self):
        value = 0
        children = []

    def __init__(self, val):
        value = val
        list = []

class SuffixTree:
    def __init__(self):
        root = Node()

    def __init__(self, val):
        root = Node(val)

    def insert(self, val):
        if self.root.value == val:
            for child in self.root.children:
                self.insert(val, child)

    def insert(self, val, node):
        if node.value == val:
            for child in node.children:
                self.insert(val, child)
        else:
            node.children.append(Node(val))
