from vertex import Vertex

class Graph:
    def __init__(self, directed=False):
        self.graph_dictionay = {}
        self.directed = directed

    def add_vertex(self, node):
        self.graph_dictionay[node.value] = node

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dictionay[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dictionay[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        pass

    def explore(self):
        print("Exploring the graph...")
        # print(self.graph_dictionay)
        current_room = self.graph_dictionay[str(list(self.graph_dictionay.keys())[0])].value
        path_total = 0
        print("\nStarting off at the {room}\n".format(room=current_room))
        while current_room != 'Treasure Room':
            node = self.graph_dictionay[current_room]
            for connected_room, weight in node.edges.items():
                key = connected_room[0]
                print("enter {0} for {1}: {2} cost".format(key.lower(), connected_room, weight))
            
            valid_choices = [str(room).lower()[0] for room in node.edges.keys()]
            # print(valid_choices)
            print("\nYou have accumulated: {0} cost".format(path_total))
            
            choice = str(input("\nWhich room do you move to? ")).lower()
            # print(choice)

            if choice not in valid_choices:
                print("please select from these letters: {0}".format(valid_choices))
            else:
                for room in node.edges.keys():
                    if room.lower().startswith(choice):
                        current_room = room
                        path_total += node.edges[room]
                print("\n*** You have chosen: {0} ***\n".format(current_room))
        print("Made it to the treasure room with {0} cost.".format(path_total))

    def print_map(self):
        print("\nMAZE LAYOUT\n")
        for node_key in self.graph_dictionay:
            print("{key} connected to...".format(key=node_key))
            node = self.graph_dictionay[node_key]
            for adjacent_node, weight in node.edges.items():
                print("=> {adj_node}: cost is {wgt}".format(adj_node=adjacent_node, wgt=weight))
            print("")
        print("")

def build_graph():
    graph = Graph()

    entrance = Vertex("Entrance")
    graph.add_vertex(entrance)
    ante_chamber = Vertex("Ante-chamber")
    graph.add_vertex(ante_chamber)
    kings_room = Vertex("King's Room")
    graph.add_vertex(kings_room)
    grand_gallery = Vertex("Grand Gallery")
    graph.add_vertex(grand_gallery)
    treasure_room = Vertex("Treasure Room")
    graph.add_vertex(treasure_room)

    graph.add_edge(grand_gallery, ante_chamber, 2)
    graph.add_edge(grand_gallery, kings_room, 2)
    graph.add_edge(treasure_room, ante_chamber, 6)
    graph.add_edge(treasure_room, grand_gallery, 4)
    graph.add_edge(entrance, ante_chamber, 7)
    graph.add_edge(entrance, kings_room, 3)
    graph.add_edge(kings_room, ante_chamber, 1)

    graph.print_map()
    return graph