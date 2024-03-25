#!/usr/bin/env python3

# author: greyshell
# description:

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def __str__(self):
        return str(self.graph)

    def degree(self, vertex):
        """
        compute the degree of a vertex
        """
        return len(self.graph[vertex])

    def max_degree(self):
        """
        compute the max degree of the graph
        """
        max_ = 0
        for _, neighbors in self.graph.items():
            degree = len(neighbors)
            if degree > max_:
                max_ = degree
        return max_

    def nos_of_self_loops(self):
        """
        count the number of self loops
        """
        count = 0
        for vertex, neighbors in self.graph.items():
            for neighbor in neighbors:
                if vertex == neighbor:
                    count += 1
        return count // 2


if __name__ == '__main__':
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

    ug = Graph(undirected_graph)
    v = 5
    print(f"compute the degree of {v}: {ug.degree(v)}")
    print(f"compute the max degree of the graph: {ug.max_degree()}")
    print(f"compute total self loops: {ug.nos_of_self_loops()}")
    print(f"string representation of graph: {ug}")
