from vertex import Vertex

class Graph:
    def __init__(self, directed=False):
        self.graph_dictionay = {}
        self.directed = directed

    def add_vertex(self, node):
        self.graph_dictionay[node.value] = node

    def add_edge(self, from_vertex, to_vertex, weight):
        from_vertex.add_edge(from_vertex.value, weight)
        if not self.directed:
            to_vertex.add_edge(to_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        pass
