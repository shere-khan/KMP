class Node:
    def __init__(self):
        self.value = 0
        self.edges = []

    def set_edges(self, edges):
        self.edges = edges

    def set_value(self, value):
        self.value = value


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

    def insert(self, pattern, value):
        tail = pattern[1:]
        # If the root has no edges (has not yet been visited)
        # create an edge and set the value of the edge to be the
        # first character of the
        if not self.root.edges:
            edge = Edge()
            edge.set_node(Node())
            edge.set_value(pattern[:1])
            self.root.edges = [edge]

            if len(tail) > 0:
                self.__insert(tail, edge.node, value)
        else:
            matched = False
            # Look for a child edge whose value matches the 1st character of
            # the pattern. If found, visit that child edge's node
            for edge in self.root.edges:
                if edge.value is pattern[0]:
                    matched = True;
                    self.__insert(tail, edge.node, value)

            # If none of the edges contain the character, then
            # create a new child edge for the root and set the value for that edge
            # to be the character. Then visit that child edge
            if not matched:
                self.__create_edge_recurse(pattern, self.root, value)

    def __insert(self, pattern, node, value):
        """

        Recursive function that inserts a pattern into the keyword tree.
        If the string is empty, that means the node value needs to be set to value, which
        is the index of the pattern in the set
        Args:
            pattern:
            node:
            value:

        """
        matched = False
        # Look for a child edge whose value matches 1st character of
        # the pattern. If found, visit that child edge's node
        for edge in node.edges:
            if edge.value is pattern[0]:
                matched = True;
                tail = pattern[1:]
                self.__insert(tail, edge.node, value)

        # If none of the edges' values match the character, then
        # create a new child edge and set the value for the new child edge
        # to be the character. Then visit that child edge
        if not matched:
            self.__create_edge_recurse(pattern, node, value)

    # Create a new child edge and set the value for the new child edge
    # to be the character. Then visit that child edge
    def __create_edge_recurse(self, pattern, node, value):
        edge = Edge()
        edge.set_node(Node())
        edge.set_value(pattern[:1])
        tail = pattern[1:]
        node.edges.append(edge)
        if len(tail) < 1:
            edge.node.set_value(value)
        else:
            self.__insert(tail, edge.node, value)

    def dfs(self, f):
        for edge in self.root.edges:
            f(edge.value)
            self.__dfs(f, edge.node)

    def __dfs(self, f, node):
        f(node.value)
        for edge in node.edges:
            f(edge.value)
            self.__dfs(f, edge.node)
