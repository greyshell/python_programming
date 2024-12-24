#!/usr/bin/env python3

# author: greyshell
from snowowl import Heap, HeapType


class WeightedEdge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __lt__(self, other_obj):
        # compare based on weight
        return self.weight < other_obj.weight

    def __gt__(self, other_obj):
        return self.weight > other_obj.weight

    def __eq__(self, other_obj):
        return self.weight == other_obj.weight

    def __ne__(self, other_obj):
        return self.weight != other_obj.weight

    def __str__(self):
        return str(self.src) + "->" + str(self.dest) + "," + " " + str(self.weight)


class MST:
    def __init__(self, graph):
        self.mst_edges = list()

        self.all_vertices = list()
        self.all_edges = list()
        # unpack the dict
        self.graph = graph

        for src, neighbors in self.graph.items():
            for node in neighbors:
                dest, weight = node[0], node[1]
                print(src, dest, weight)
                exit(0)

        # for src, value in self.graph.items():
        #     # unpack the list
        #     for item in value:
        #         # unpack the dict
        #         for dest, weight in item.items():  # O(1) -> dict has only 1 key
        #             self.all_edges.append(WeightedEdge(src, dest, weight))
        #
        #             # compute vertices
        #             if src not in self.all_vertices:
        #                 self.all_vertices.append(src)
        #             if dest not in self.all_vertices:
        #                 self.all_vertices.append(dest)

    def get_all_edges(self):
        return self.all_edges

    def get_all_vertices(self):
        return self.all_vertices

    def prims_lazy(self):
        """
        the algorithm returns the mst edges -> list of WeightedEdge objects
        """
        start_vertex_edge_obj = self.all_edges[0]

        # track the visited vertices
        visited = set()
        # add the source vertex into the visited set
        visited.add(start_vertex_edge_obj.src)

        arr = list()
        priority_queue = Heap(arr, HeapType.MIN)

        # add the start vertex edge into the min priority queue
        priority_queue.insert(start_vertex_edge_obj)

        while priority_queue:
            # pop the min weight vertex from the queue
            vertex_edge_obj = priority_queue.remove()
            # print(vertex, end=" ")
            self.mst_edges.append(vertex_edge_obj)
            # iterate all neighbors of that node
            neighbors_edge_obj = self.graph[vertex_edge_obj.src]

            for neighbor in neighbors_edge_obj:
                dest_vertex = neighbor.src
                print(dest_vertex)
            exit(0)


    def get_mst_weight(self):
        # iterate all the edges and find the weight
        sum_ = 0
        for mst_edge in self.mst_edges:
            sum_ = sum_ + mst_edge.weight

        return sum_


if __name__ == '__main__':
    # dict representation
    # ref: Sedgewick Algorithms 4th edition, page: 614
    uwg = {
        # source_node: [[dest_node, weight], [dest_node, weight]]
        0: [[7, 0.16], [4, 0.38], [2, 0.26]],
        1: [[5, 0.32], [7, 0.19], [1, 0.36], [3, 0.29]],
        2: [[3, 0.17], [7, 0.34]],
        3: [[6, 0.52]],
        4: [[5, 0.35], [7, 0.37]],
        5: [[7, 0.28]],
        6: [[2, 0.40], [0, 0.58], [4, 0.93]],
    }

    g = MST(uwg)
    g.prims_lazy()

    # # check edges are loaded properly
    # vertices = g.get_all_vertices()
    # print(vertices)
    # print("")
    #
    # edges = g.get_all_edges()
    # for edge in edges:
    #     print(edge)
    # print("")
    #
    # # check not equal operator
    # if edges[0] != edges[1]:
    #     print("edges weight do not match")
    #
    # # check equal operator
    # if edges[0] == edges[1]:
    #     print("edges weight match")
    # else:
    #     print("edges weight do not match")
    #
    # # check greater than operator
    # if edges[0] > edges[1]:
    #     print("edges[0] weight greater than edges[1]")
    # else:
    #     print("edges[1] weight greater than edges[0]")
    #
    # # check less than operator
    # if edges[0] < edges[1]:
    #     print("edges[0] weight less than edges[1]")
    # else:
    #     print("edges[1] weight less than edges[0]")
    #
    # # find min edges from all edges to check obj compare working
    # min_edge = edges[0]
    # for edge in edges:
    #     if edge.weight < min_edge.weight:
    #         min_edge = edge
    #
    # print("")
    # print(f"min edge: {min_edge}")



