#!/usr/bin/env python3

# author: greyshell
# reference: grokking algorithm by Aditya Y. Bhargava,
# problem: trading a piano, page 122

from typing import List
from collections import deque


# definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

    # display the node
    def __repr__(self):
        s = str(self.val) + ":"
        for n in self.neighbors:
            s += str(n.val) + " "
        return s


class Graph:
    def __init__(self, usr_inp, start_node=0):
        # create a graph
        self._graph = dict()

        for i, neighbours in enumerate(usr_inp, start=start_node):
            self._graph[i] = []
            for node in neighbours:
                self._graph[i].append(node)

    def get(self):
        return self._graph


def bfs(graph: dict, start_node) -> None:
    """
    bfs approach
    """
    # add the first node into visited dict
    visited = {start_node: True}

    # add the first node into the queue
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        # iterate all neighbors of that node
        for neighbor_node in graph[node]:
            # if that neighbor node is not visitied then add to the visited dict and queue
            if not visited.get(neighbor_node, False):
                visited[neighbor_node] = True
                queue.append(neighbor_node)


def main():
    # build a graph
    # case 01: user input is dict
    user_input_01 = {
        2: [0, 3],
        3: [],
        0: [1, 2],
        1: [2]
    }

    user_input_02 = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    bfs(user_input_02, start_node='A')
    exit(0)

    # case 02: user input is a list[list[int]]
    user_input_03 = [[2, 4], [1, 3], [2, 4], [1, 3]]

    g = Graph(user_input_03, start_node=1)
    # returns the dict
    graph = g.get()
    print(graph)
    start_node = list(graph.keys())[0]
    bfs(graph, start_node)


if __name__ == '__main__':
    main()

