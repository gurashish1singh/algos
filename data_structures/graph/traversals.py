from __future__ import annotations

from collections import deque
from typing import (
    Set,
    Union,
)

GRAPH = dict[Union[str, int], list[Union[str, int]]]
NODE = Union[str, int]


def depth_first_traversal(graph: GRAPH, source_node: NODE) -> None:
    # FIFO
    stack = [source_node]
    while stack:
        current = stack.pop()
        print(current)
        # Sanity check
        if current in graph:
            # Consider the neighbours of current now
            neighbours = graph[current]
            stack.extend(neighbours)


def breadth_first_traversal(graph: GRAPH, source_node: NODE) -> None:
    # FILO
    queue = deque()
    queue.append(source_node)
    while queue:
        current = queue.popleft()
        print(current)
        if current in graph:
            neighbours = graph[current]
            queue.extend(neighbours)


def find_path_using_dfs(graph: GRAPH, source: NODE, destination: NODE) -> bool:
    # n -> number of nodes
    # n^2 -> number of edges
    # Time: O(n^2)
    # Space: O(n)
    # This code assumes that the graph is acyclic, as in we are not going to be trapped
    # in an infinite loop
    if source not in graph:
        return False
    elif source == destination:
        return True

    neighbours = graph[source]
    for neighbour in neighbours:
        if find_path_using_dfs(graph, neighbour, destination):
            return True
    return False


def find_path_using_bfs(graph: GRAPH, source: NODE, destination: NODE) -> bool:
    # n -> number of nodes
    # n^2 -> number of edges
    # Time: O(n^2)
    # Space: O(n)
    # This code assumes that the graph is acyclic, as in we are not going to be trapped
    # in an infinite loop
    if source not in graph:
        return False
    elif source == destination:
        return True

    queue = deque()
    queue.append(source)
    while queue:
        current = queue.popleft()
        if current == destination:
            return True
        neighbours = graph[current]
        queue.extend(neighbours)
    return False


def find_path_using_dfs_for_acyclic_graph(
    graph: GRAPH, source: NODE, destination: NODE, seen: Set[NODE]
) -> bool:
    # We use a set (seen) to keep track of the visited nodes to avoid infinite loops
    # Time and space complexity will be the same as find_path_using_dfs
    if source == destination:
        return True
    elif source not in graph:
        return False
    elif source in seen:
        return False

    seen.add(source)
    neighbours = graph[source]
    for neighbour in neighbours:
        if find_path_using_dfs_for_acyclic_graph(graph, neighbour, destination, seen):
            return True
    return False


def find_path_using_bfs_for_acyclic_graph(graph: GRAPH, source: NODE, destination: NODE) -> bool:
    # We use a set (seen) to keep track of the visited nodes to avoid infinite loops
    # Time and space complexity will be the same as find_path_using_bfs
    if source == destination:
        return True
    elif source not in graph:
        return False

    seen = set()
    queue = deque(source)
    while queue:
        current = queue.popleft()
        if current not in seen:
            if current == destination:
                return True
            neighbours = graph[current]
            queue.extend(neighbours)
            seen.add(current)
    return False


def convert_edge_list_to_adjacency_list(edge_list: list[list[NODE]]) -> GRAPH:
    graph = {}
    for edge in edge_list:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def counting_connected_components(graph: GRAPH) -> int:
    # Time and space complexity will be same as find_path_using_dfs
    count = 0
    seen = set()
    for node in graph:
        if explore_neighbours(graph, node, seen):
            count += 1
    return count


def explore_neighbours(graph: GRAPH, node: NODE, seen: Set[NODE]) -> bool:
    # Using DFS we get all neighbours of a node. If the node is already visited
    # we return False, and we return True when we visit each node atmost once.
    if node in seen:
        return False

    seen.add(node)
    for neighbour in graph[node]:
        explore_neighbours(graph, neighbour, seen)
    return True


def largest_connected_components(graph: GRAPH) -> int:
    # Time and space complexity will be same as find_path_using_dfs
    # We consider the number of nodes here instead of the number of edges
    size = 0
    seen = set()
    for node in graph:
        size = max(size, explore_size(graph, node, seen))
    return size


def explore_size(graph: GRAPH, node: NODE, seen: Set[NODE]) -> int:
    # Using DFS we get travel to all neighours of a node. If the node is already visited
    # we return 0, else we add the number of unique neighbours to the size variable and return it.
    if node in seen:
        return 0

    # This represents the current node
    size = 1
    seen.add(node)
    for neighbour in graph[node]:
        size += explore_size(graph, neighbour, seen)
    return size


def get_shortest_path_using_bfs(graph: GRAPH, source: NODE, destination: NODE) -> int:
    # Time complexity is O(n) since we only traverse through the graph once
    if source not in graph:
        return -1
    elif source == destination:
        return 0

    seen = set(source)
    queue = deque()
    queue.append((source, 0))
    while queue:
        current_node, current_distance = queue.popleft()
        if current_node == destination:
            return current_distance
        for neighbour in graph[current_node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append((neighbour, current_distance + 1))
    return -1


if __name__ == "__main__":
    # Adjacency List
    # graph = {
    #     "a": ["c", "b"],
    #     "b": ["d"],
    #     "c": ["e"],
    #     "d": ["f"],
    #     "e": [],
    #     "f": [],
    # }

    # depth_first_traversal(graph, "a")
    # print("*" * 80)
    # breadth_first_traversal(graph, "a")

    # Directed paths
    # graph = {
    #     "f": ["g", "i"],
    #     "g": ["h"],
    #     "h": [],
    #     "i": ["g", "k"],
    #     "j": ["i"],
    #     "k": [],
    # }
    # print(find_path_using_dfs(graph, "f", "k"))
    # print("*" * 80)
    # print(find_path_using_bfs(graph, "f", "k"))

    # Undirected paths
    # edge_list = [
    #     ["i", "j"],
    #     ["k", "i"],
    #     ["m", "k"],
    #     ["k", "l"],
    #     ["n", "o"],
    # ]
    # graph = convert_edge_list_to_adjacency_list(edge_list)
    # print(graph)
    # print(find_path_using_dfs_for_acyclic_graph(graph, "i", "m", set()))
    # print("*" * 80)
    # print(find_path_using_bfs_for_acyclic_graph(graph, "i", "m"))

    # Counting connected components
    # graph = {
    #     0: [8, 1, 5],
    #     2: [3, 4],
    #     1: [0],
    #     5: [0, 8],
    #     8: [0, 5],
    #     3: [2, 4],
    #     4: [3, 2],
    # }
    # print(counting_connected_components(graph))
    # print("*" * 80)
    # print(largest_connected_components(graph))

    # Finding the shortest path
    graph = {
        "w": ["x", "v"],
        "v": ["w", "z"],
        "x": ["w", "y"],
        "y": ["x", "z"],
        "z": ["v", "y"],
    }
    print(get_shortest_path_using_bfs(graph, "w", "z"))
