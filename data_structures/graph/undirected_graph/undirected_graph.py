
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []  # no duplicate neighbors

    def add_neighbor(self, name):
        self.neighbors.append(name)

    def __str__(self):
        result = str(self.name)
        result += ": {"
        for neighbor in self.neighbors:
            result += str(neighbor) + ","

        # when the vertex / node has neighbors, remove the last ',' char
        if result[-1] == ',':
            result = result[:-1]

        result += "}"
        return result


class UndirectedGraph:

    def __init__(self):
        # key: name of the vertex
        # value: obj of the vertex
        self.vertices = {}

    def add_vertex(self, vertex_name):
        self.vertices[vertex_name] = Vertex(vertex_name)

    def add_edge(self, from_vertex_name, to_vertex_name):
        if from_vertex_name not in self.vertices or \
                to_vertex_name not in self.vertices:
            raise ValueError("invalid vertex name")

        self.vertices[from_vertex_name].add_neighbor(to_vertex_name)
        # self.vertices[to_vertex_name].add_neighbor(from_vertex_name)

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_edges(self):
        edges = []

        for src_vertex, src_vertex_obj in self.vertices.items():
            neighbors = src_vertex_obj.neighbors
            for neighbor in neighbors:
                edges.append((src_vertex, neighbor))

        return edges  # returns list of tuples

    # auxiliary methods
    def get_degree(self, vertex_name):
        """
        time complexity: O(E), where E is the edges of that vertex
        """
        return len(self.vertices[vertex_name].neighbors)


def demo_vertex():
    print(f"[+] Demo the vertex class")
    v = Vertex("A")
    print(f"{v.__repr__()}")  # print the obj address
    print(f"{v}")  # if __str__() method is available then call that method else print obj address

    b_obj = Vertex("B")  # create a vertex object of B
    v.add_neighbor(b_obj.name)
    v.add_neighbor(Vertex("C").name)  # alternate way

    print(v.__repr__())
    print(v)
    print("")


def demo_undirected_graph():
    print(f"[+] Demo undirected graph")
    ug = UndirectedGraph()

    # ref: Sedgewick Algorithms 4th edition, page 522
    # add vertices
    for src_vertex in range(13):
        ug.add_vertex(src_vertex)

    print(f"vertices:")
    print(f"{ug.get_vertices()}")

    # add edges
    ug.add_edge(0, 1)
    ug.add_edge(1, 0)

    ug.add_edge(0, 2)
    ug.add_edge(2, 0)

    ug.add_edge(0, 5)
    ug.add_edge(5, 0)

    ug.add_edge(0, 6)
    ug.add_edge(6, 0)

    ug.add_edge(6, 4)
    ug.add_edge(4, 6)

    ug.add_edge(4, 3)
    ug.add_edge(3, 4)

    ug.add_edge(4, 5)
    ug.add_edge(5, 4)

    ug.add_edge(5, 3)
    ug.add_edge(3, 5)

    ug.add_edge(7, 8)
    ug.add_edge(8, 7)

    ug.add_edge(9, 10)
    ug.add_edge(10, 9)

    ug.add_edge(9, 11)
    ug.add_edge(11, 9)

    ug.add_edge(9, 12)
    ug.add_edge(12, 9)

    ug.add_edge(11, 12)
    ug.add_edge(12, 11)

    # print edges
    print("")
    print(f"edges:")
    edges = ug.get_edges()
    for e in edges:
        print(f"({e[0]}, {e[1]})", end=", ")

    # get the degree of each vertex
    print("\n")
    for vertex_name in ug.get_vertices():
        # for undirected graph, total degree is equal to in_degree or out_degree
        degree = ug.get_degree(vertex_name)
        print(f"degree of node '{vertex_name}': {degree}")


if __name__ == '__main__':
    # demo_vertex()
    # demo_undirected_graph()

    # ref: Sedgewick Algorithms 4th edition, page 522
    # dict representation
    undirected_graph = {
        0: [1, 2, 5],
        1: [0],
        2: [0],
        3: [4, 5],
        4: [3, 5, 6],
        5: [0, 3, 4],
        6: [0, 4]
    }

    print(f"vertices:")
    print(f"{list(undirected_graph.keys())}")
    print(f"edges:")
    for vertex, neighbours in undirected_graph.items():
        print(f"{vertex}: {neighbours}")
