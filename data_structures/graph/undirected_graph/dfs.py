#!/usr/bin/env python3

# author: greyshell
# description: dfs traversals on a connected undirected graph

from collections import deque


def dfs_recursive(undirected_graph, start_vertex, visited):
    """
    time: O(V + E)
    space: O(V), call stack depth
    """
    if start_vertex not in undirected_graph.keys():
        raise ValueError("Vertex not found")

    visited.append(start_vertex)
    neighbors = undirected_graph[start_vertex]

    for neighbor in neighbors:
        if neighbor not in visited:
            dfs_recursive(undirected_graph, neighbor, visited)

    return visited


def dfs(undirected_graph, start_vertex):
    """
    depth first search
    time complexity: O(V + E)
    space complexity: O(V) -> to maintain the visited set
    """
    # check if the start vertex_name is present in the graph
    if start_vertex not in undirected_graph.keys():
        raise ValueError("Vertex not found")

    # track the visited vertices
    visited = []

    # add the start vertex_name into the stack
    stack = deque()
    stack.append(start_vertex)

    while stack:  # check if stack is not empty
        # pop the vertex name from the stack but don't process that immediately
        vertex = stack.pop()
        # check if the vertex_name is not in visited set then add into the visited set and process
        if vertex not in visited:
            visited.append(vertex)
            # iterate all neighbors of that vertex
            neighbors = undirected_graph[vertex]
            # iterate the neighbor from reverse order to match the recursive version
            # for i in range(len(neighbors) - 1, -1, -1):

            for neighbor in neighbors:
                # if that neighbor is not in the visited set then add that into the stack
                # neighbor = neighbors[i]
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


if __name__ == '__main__':
    # ref: Sedgewick Algorithms 4th edition, page 532
    ug = {
        0: [2, 1, 5],
        1: [0, 2],
        2: [0, 1, 3, 4],
        3: [5, 4, 2],
        4: [3, 2],
        5: [3, 0]
    }

    start = 0
    result_visited_nodes = []
    print(f"dfs traversal recursive: ")
    print(dfs_recursive(ug, start, result_visited_nodes))  # output: [0, 2, 1, 3, 5, 4]

    print("")
    print(f"dfs traversal iterative: ")
    print(dfs(ug, start))
