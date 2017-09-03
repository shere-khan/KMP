class Node:
    def __init__(self):
        # self.value = 0
        # self.children = []
        self.edges = []

    def set_edges(self, edges):
        self.edges = edges


class Edge:
    def __init__(self):
        self.node = None
        self.value = None

    def set_value(self, value):
        self.value = value

    def set_node(self, node):
        self.node = node


class KeywordTree:
    def __init__(self):
        self.root = Node()
        self.value = None

    def setValue(self, val):
        self.value = val

    def insert(self, pattern):
        tail = pattern[1:]
        if not self.root.edges:
            edge = Edge()
            edge.set_node(Node())
            edge.set_value(pattern[:1])
            self.root.edges = [edge]

            if len(tail) > 0:
                self.__insert(tail, self.root.edges[0].node)
        else:
            for edge in self.root.edges:
                if edge.value is pattern[0]:
                    self.__insert(tail, edge.node)

    def __insert(self, pattern, node):
        tail = pattern[1:]
        matched = False
        for edge in node.edges:
            if edge.value is pattern[0]:
                matched = True;
                self.__insert(tail, edge.node)

        if not matched:
            edge = Edge()
            edge.node = Node()
            edge.set_value(pattern[:1])
            node.edges.append(edge)

            if len(tail) > 0:
                self.__insert(tail, edge.node)

    def inorder(self, f):
        for edge in self.root.edges:
            f(edge.value)
            self.__inorder(f, edge.node)

    def __inorder(self, f, node):
        for edge in node.edges:
            f(edge.value)
            self.__inorder(f, edge.node)
