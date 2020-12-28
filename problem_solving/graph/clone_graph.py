#!/usr/bin/env python3

# author: greyshell
# reference: https://leetcode.com/problems/clone-graph/

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


# helper fucntion to build the nodes from user input
def build_graph_from_nodes(user_input: List[List[int]]):
    """
    build a graph by wiring all node objects and return a start node
    """
    lookup = {}
    # create all node obj but with empty neighbour node list
    for i, _ in enumerate(user_input, start=1):
        obj = Node(i, [])
        lookup[i] = obj

    # update all node obj with their neighbour obj address
    for i, nodes in enumerate(user_input, start=1):
        for n in nodes:
            # get the neighbour node based on the index and update the list
            obj = lookup.get(n, False)
            if obj:
                lookup[i].neighbors.append(obj)

    # return the first node
    return lookup[1]


class Solution(object):
    def cloneGraph(self, node: Node) -> Node:
        """
        bfs approach
        """
        # when the start node is empty
        if not node:
            return node

        # dictionary to save the visited node and it's respective clone as key and value respectively
        # this helps to avoid cycles
        visited = {}

        # put the first node in the queue
        queue = deque([node])
        # create a new node / clone with same start_node val but empty neighbours becuse we don't know their address
        # put that new node in the visited dictionary
        visited[node] = Node(node.val, [])

        # perform bfs traversal
        while queue:  # if queue is not empty
            # dequeue / pop a node
            n = queue.popleft()

            # iterate through its neighbors
            for neighbor_node in n.neighbors:
                if neighbor_node not in visited:
                    # create a new node / clone
                    visited[neighbor_node] = Node(neighbor_node.val, [])
                    # add the newly encountered node to the queue
                    queue.append(neighbor_node)

                # get the clone node of the original from visit dict
                visited[n].neighbors.append(visited[neighbor_node])

        return visited[node]


def main():
    user_input = [[2, 4], [1, 3], [2, 4], [1, 3]]
    start_node = build_graph_from_nodes(user_input)
    print(f"start node = {start_node}")

    s = Solution()
    out = s.cloneGraph(start_node)
    print(f"start node = {out}")


if __name__ == '__main__':
    main()
