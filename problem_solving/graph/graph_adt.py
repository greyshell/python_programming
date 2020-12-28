#!/usr/bin/env python3

# author: greyshell
# description: graph adt

from typing import List
from collections import deque


class Vertex:
    """
    implementation of a vertex / node of a DAG
    """

    def __init__(self, key):
        self._key = key
        self._neighbors = []

    def add_neighbor(self, neighbor_vertex, weight):
        self._neighbors.append((neighbor_vertex, weight))

    def get_key(self):
        return self._key

    def get_connections(self):
        return self._neighbors

    def get_weight(self, to_vertex):
        for neighbor in self._neighbors:
            if to_vertex == neighbor[0].get_key():
                return neighbor[1]


class Graph(object):
    """
    implementation of DAG ADT
    """

    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self._graph = {}
            self._vertices = {}
        else:
            self._graph = graph_dict
            # add vertices
            for v in self._graph:
                self.add_vertex(v)
            # add edges
            for v in self._graph:
                for e in self._graph[v]:
                    self.add_edge(v, e[0], e[1])

    def add_vertex(self, vertex):
        v = Vertex(vertex)
        self._vertices[vertex] = v

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self._vertices:
            self.add_vertex(from_vertex)

        if to_vertex not in self._vertices:
            self.add_vertex(to_vertex)

        self._vertices[from_vertex].add_neighbor(self._vertices[to_vertex], weight)

    def get_vertices(self):
        vertices = []
        for v in self._vertices.keys():
            vertices.append(v)
        return vertices

    def get_vertex(self, vertex_key):
        for vertex in self._vertices:
            if vertex == vertex_key:
                return self._vertices[vertex]

    def get_edges(self):
        edges = []
        for vertex in self._vertices:
            neighbors = self._vertices[vertex].get_connections()

            for neighbor in neighbors:
                to_vertex = neighbor[0].get_key()
                edges.append((vertex, to_vertex, self._vertices[vertex].get_weight(to_vertex)))

        return edges

    def BFS(self, start_vertex=None):
        # TBD
        start_vertex = self.get_vertex(start_vertex)

        if start_vertex is None:
            raise Exception(f"vertex: {start_vertex} is not found in graph")

        visited = [False] * len(self._vertices)
        traversed = []

        q = Queue()
        q.enqueue(start_vertex)

        while not q.isEmpty():
            v = q.dequeue()
            key = v.get_key()

            if not visited[key]:
                visited[key] = True
                traversed.append(key)

                for neighbor in v.get_connections():
                    if not visited[neighbor[0].get_key()]:
                        q.enqueue(neighbor[0])

        return traversed


def main():
    g = Graph()

    # add vertex
    for v in range(0, 5):
        g.add_vertex(v)

    # add edges
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(2, 4, 6)
    g.add_edge(4, 3, 1)

    print(f"vertices: {g.get_vertices()}")
    print(f"edges: {g.get_edges()}")
    print(f"bfs: the nodes traversed from {0} are: {g.BFS(0)}")

    print("")
    # taking graph as a dictionary
    # d = {
    #     "0": [("1", 5), ("2", 3)],
    #     "1": [("3", 3)],
    #     "2": [("1", 2), ("3", 5), ("4", 6)],
    #     "3": [],
    #     "4": [("3", 1)]
    # }
    #
    # g1 = Graph(graph_dict=d)
    # print(f"vertices: {g1.get_vertices()}")
    # print(f"edges: {g1.get_edges()}")


if __name__ == '__main__':
    main()
