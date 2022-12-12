from __future__ import annotations

from collections import defaultdict


class DirectedGraph:
    def __init__(self, edges: list[tuple[str, str]]) -> None:
        self.edges = edges
        self.graph_dict = defaultdict(list)
        for start, end in edges:
            self.graph_dict[start].append(end)
        print(self.graph_dict)

    def get_paths(self, start: str, end: str, path: list[str]) -> list[list[str]]:
        if start not in self.graph_dict:
            return []

        path = path + [start]
        if start == end:
            return [path]

        paths = []
        for node in self.graph_dict[start]:
            # Only if we have never visited the node, we search for paths again
            if node not in path:
                paths += self.get_paths(start=node, end=end, path=path)
        return paths

    def get_shortest_path(self, start: str, end: str, path: list[str]) -> list[str]:
        # Not weighted, only deals with number of items in list
        if start not in self.graph_dict:
            return []

        path = path + [start]
        if start == end:
            return path

        shortest_path = []
        for node in self.graph_dict[start]:
            # Only if we have never visited the node, we search for paths again
            if node not in path:
                sp = self.get_shortest_path(start=node, end=end, path=path)
                if sp:
                    if not shortest_path or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    dg = DirectedGraph(routes)

    iters = (
        ("Toronto", "Mumbai", []),
        ("Mumbai", "Mumbai", [["Mumbai"]]),
        ("Mumbai", "Paris", [["Mumbai", "Paris"]]),
        (
            "Mumbai",
            "New York",
            [
                ["Mumbai", "Paris", "Dubai", "New York"],
                ["Mumbai", "Paris", "New York"],
                ["Mumbai", "Dubai", "New York"],
            ],
        ),
    )
    for start, end, expected_path in iters:
        print(f"{start = }, {end = }, paths = {dg.get_paths(start, end, [])}")
        assert (
            dg.get_paths(start, end, []) == expected_path
        ), f"{expected_path = } not equal to returned path = {dg.get_paths(start, end, [])}"

    iters = (
        ("Toronto", "Mumbai", []),
        ("Mumbai", "Mumbai", ["Mumbai"]),
        ("Mumbai", "Paris", ["Mumbai", "Paris"]),
        ("Mumbai", "New York", ["Mumbai", "Paris", "New York"]),
    )
    for start, end, expected_path in iters:
        print(f"{start = }, {end = }, paths = {dg.get_shortest_path(start, end, [])}")
        assert (
            dg.get_shortest_path(start, end, []) == expected_path
        ), f"{expected_path = } not equal to returned path = {dg.get_shortest_path(start, end, [])}"
