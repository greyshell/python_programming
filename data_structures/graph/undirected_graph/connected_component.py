#!/usr/bin/env python3

# author: greyshell
# description: find connected component in an undirected graph

from collections import deque, defaultdict, Counter


class ConnectedComponent:
    def __dfs(self, vertex):
        self.visited.add(vertex)
        self.component_table[vertex] = self.count
        neighbors = self.undirected_graph[vertex]

        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.__dfs(neighbor)

    def __init__(self, undirected_graph):
        self.undirected_graph = undirected_graph
        self.component_table = dict()  # key: vertex, value: component_id
        self.visited = set()
        self.count = 0

        for vertex in self.undirected_graph.keys():
            if vertex not in self.visited:
                self.__dfs(vertex)
                self.count += 1

    def is_connected(self, src_vertex, dst_vertex):
        if (src_vertex not in self.undirected_graph.keys() or
                dst_vertex not in self.undirected_graph.keys()):
            return False

        return self.component_table.get(src_vertex) == self.component_table.get(dst_vertex)

    def get_component_table(self):
        result = defaultdict(list)

        for vertex, component_id in self.component_table.items():
            result[component_id].append(vertex)
        return result


if __name__ == '__main__':
    # ref: Sedgewick Algorithms 4th edition, page 544
    # dict representation
    UG = {
        0: [1, 2, 5, 6],
        1: [0],
        2: [0],
        3: [4, 5],
        4: [3, 5, 6],
        5: [0, 3, 4],
        6: [0, 4],
        7: [8],
        8: [7],
        9: [10, 11, 12],
        10: [9],
        11: [9, 12],
        12: [9, 11]
    }
    cc = ConnectedComponent(UG)

    print(f"[+] Total connected component[s]: {cc.count}")

    node = 9
    print(f"[+] node: {node}, component id: {cc.component_table.get(node, None)}")

    src_v = 9
    dst_v = 12
    print(f"[+] Is {src_v} connected with {dst_v} ? {cc.is_connected(src_v, dst_v)}")

    print(f"[+] Component Table: {cc.get_component_table()}")
