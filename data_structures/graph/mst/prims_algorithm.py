
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
    # dict representation
    # pg: 614
    ewg = {
        # source_node: [{dest_node: weight}, {dest_node: weight}]
        0: [{2: 0.26}, {4: 0.38}],
        1: [{7: 0.19}],
        2: [{7: 0.34}],
        3: [],
        4: [{7: 0.37}],
        5: [{7: 0.28}],
        6: [{0: 0.58}],
        7: []
    }

    print(f"{ewg}")