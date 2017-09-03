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
            matched = False
            # Look for a child edge whose value matches the 1st character of
            # the pattern. If found, visit that child edge's node
            for edge in self.root.edges:
                if edge.value is pattern[0]:
                    matched = True;
                    self.__insert(tail, edge.node)

            # If none of the edges contain the character, then
            # create a new child edge for the root and set the value for that edge
            # to be the character. Then visit that child edge
            if not matched:
                self.__create_edge_recurse(pattern, self.root)

    def __insert(self, pattern, node):
        matched = False
        # Look for a child edge whose value matches 1st character of
        # the pattern. If found, visit that child edge's node
        for edge in node.edges:
            if edge.value is pattern[0]:
                matched = True;
                self.__insert(pattern[1:], edge.node)

        # If none of the edges' values match the character, then
        # create a new child edge and set the value for the new child edge
        # to be the character. Then visit that child edge
        if not matched:
            self.__create_edge_recurse(pattern, node)

    # Create a new child edge and set the value for the new child edge
    # to be the character. Then visit that child edge
    def __create_edge_recurse(self, pattern, node):
        edge = Edge()
        edge.set_node(Node())
        edge.set_value(pattern[:1])
        node.edges.append(edge)

        tail = pattern[1:]
        if len(tail) > 0:
            self.__insert(tail, edge.node)

    def dfs(self, f):
        for edge in self.root.edges:
            f(edge.value)
            self.__dfs(f, edge.node)

    def __dfs(self, f, node):
        for edge in node.edges:
            f(edge.value)
            self.__dfs(f, edge.node)
