#!/usr/bin/env python3

# author: greyshell
# description: bfs traversals on a connected undirected graph

from collections import deque


def bfs(undirected_graph, start_vertex):
    """
    Breadth first search
    time complexity: O(V + E)
    space complexity: O(V) -> to maintain the visited set
    """
    result = []
    # check if the start vertex_name is present in the graph
    if start_vertex not in undirected_graph.keys():
        raise ValueError("Vertex not found")

    # track the visited vertices
    visited = set()
    # add the source vertex into the visited set
    visited.add(start_vertex)

    # add the start vertex_name into the queue
    queue = deque()
    queue.append(start_vertex)

    while queue:
        # pop the vertex from the queue
        vertex = queue.popleft()
        # print(vertex, end=" ")
        result.append(vertex)
        # iterate all neighbors of that node
        neighbors = undirected_graph[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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

    print(f"[+] bfs traversal: ")
    print(f"[+] BFS: single source shortest path")
    print(bfs(UG, start_vertex=0))
