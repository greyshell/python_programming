#!/usr/bin/env python3

# author: greyshell
# description: dfs traversals on a connected undirected graph

from collections import deque

# visited = list()


def dfs_recursive(undirected_graph, vertex):
    """
    time: O(V + E)
    space: O(V)
    """
    global node_visited

    if vertex not in undirected_graph.keys():
        raise ValueError("Vertex not found")

    node_visited.append(vertex)
    neighbors = undirected_graph[vertex]

    for neighbor in neighbors:
        if neighbor not in node_visited:
            dfs_recursive(undirected_graph, neighbor)


def dfs(undirected_graph, vertex) -> list:
    """
    depth first search
    time complexity: O(V + E)
    space complexity: O(V) -> to maintain the visited set
    """
    # check if the start vertex_name is present in the graph
    if vertex not in undirected_graph.keys():
        raise ValueError("Vertex not found")

    # track the visited vertices
    visited = list()

    # add the start vertex_name into the stack
    stack = deque()
    stack.append(start_vertex)

    while stack:
        # pop the vertex name from the stack but don't process that immediately
        vertex = stack.pop()
        # check if the vertex_name is not in visited set then add into the visited set and process
        if vertex not in visited:
            visited.append(vertex)
            # iterate all neighbors of that vertex
            neighbors = undirected_graph[vertex]
            for neighbor in neighbors:
                # if that neighbor is not in the visited set then add that into the stack
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


if __name__ == '__main__':
    # ref: Sedgewick Algorithms 4th edition, page 532
    ug = {
        0: [1, 2, 5],
        1: [0, 2],
        2: [0, 1, 4],
        3: [2, 4, 5],
        4: [2, 3],
        5: [0, 3]
    }

    print(f"dfs traversal: ")
    start_vertex = 0
    node_visited = list()
    dfs_recursive(ug, start_vertex)
    print(node_visited)

    print(dfs(ug, start_vertex))


