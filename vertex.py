class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, adjacent_value, weight=0):
        self.edges[adjacent_value] = weight
        print("Added {edge} as a connection to {this_vert}"
        .format(edge=adjacent_value, this_vert=self.value))

    def get_edges(self):
        return self.edges.keys()
