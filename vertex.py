class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, vertex):
        self.edges.append(vertex.value)
        print("Added {edge} as a connection to {this_vert}"
        .format(edge=vertex.value, this_vert=self.value))

    def list_edges(self):
        for edge in self.edges:
            print(edge + "\n")


''' Test / Debug '''
kings_hwy = Vertex("Kings Hwy")
rockaway = Vertex("Rockaway")
ave_h = Vertex("Ave. H")
bedford = Vertex("Bedford Ave.")
utica = Vertex("Utica Ave.")
coney = Vertex("Coney Island")

kings_hwy.add_edge(utica)
kings_hwy.add_edge(ave_h)
kings_hwy.add_edge(rockaway)
bedford.add_edge(utica)
ave_h.add_edge(kings_hwy)
ave_h.add_edge(rockaway)
rockaway.add_edge(kings_hwy)
rockaway.add_edge(ave_h)
rockaway.add_edge(coney)
utica.add_edge(bedford)
utica.add_edge(kings_hwy)
utica.add_edge(coney)
coney.add_edge(utica)
coney.add_edge(rockaway)

utica.list_edges()