#!/usr/bin/env python3

# author: greyshell
# description: dfs traversals on a connected undirected graph

from collections import deque


def dfs(undirected_graph, start_vertex):
    """
    depth first search
    time complexity: O(V + E)
    space complexity: O(V) -> to maintain the visited set
    """
    result = []
    # check if the start vertex_name is present in the graph
    if start_vertex not in undirected_graph.keys():
        raise ValueError("Vertex not found")

    # track the visited vertices
    visited = set()

    # add the start vertex_name into the stack
    stack = deque()
    stack.append(start_vertex)

    while stack:
        # pop the vertex name from the stack but don't process that immediately
        vertex = stack.pop()
        # check if the vertex_name is not in visited set then add into the visited set and process
        if vertex not in visited:
            visited.add(vertex)
            # print(vertex, end=" ")
            result.append(vertex)
            # iterate all neighbors of that vertex
            neighbors = undirected_graph[vertex]
            for neighbor in neighbors:
                # if that neighbor is not in the visited set then add that into the stack
                if neighbor not in visited:
                    stack.append(neighbor)
    return result


if __name__ == '__main__':
    # ref: Sedgewick Algorithms 4th edition, page 532
    UG = {
        0: [1, 2, 5],
        1: [0, 2],
        2: [0, 1, 4],
        3: [2, 4, 5],
        4: [2, 3],
        5: [0, 3]
    }

    print(f"dfs traversal: ")
    print(dfs(UG, start_vertex=0))
