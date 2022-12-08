from __future__ import annotations

from typing import Set


class AdjacencyListVertex:
    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbours: Set[AdjacencyListVertex] = set()

    def add_neighbour(self, vertex: AdjacencyListVertex) -> None:
        self.neighbours.add(vertex)


class AdjacencyMatrixVertex:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"vertex_{self.name}"


class AdjacencyListUndirectedGraph:
    def __init__(self) -> None:
        self.vertices: dict[str, AdjacencyListVertex] = {}

    def add_vertex(self, vertex: AdjacencyListVertex) -> None:
        if isinstance(vertex, AdjacencyListVertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def add_edge(self, u: AdjacencyListVertex, v: AdjacencyListVertex) -> None:
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbour(v)
            self.vertices[v].add_neighbour(u)

    def pp(self) -> None:
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbours)))


class AdjacencyMatrixUndirectedGraph:
    def __init__(self) -> None:
        self.vertices: dict[str, AdjacencyMatrixVertex] = {}
        self.edges: list[list[int]] = []
        self.edge_indices: dict[str, int] = {}

    def add_vertex(self, vertex: AdjacencyMatrixVertex) -> None:
        if isinstance(vertex, AdjacencyMatrixVertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            # Add columns of 0s based on the vertex
            for row in self.edges:
                row.append(0)
            # Add rows of 0s to the matrix based on the vertex
            self.edges.append([0] * (len(self.edges) + 1))
            # Assign a row index based on how many vertices are being added to the matrix
            self.edge_indices[vertex.name] = len(self.edge_indices)

    def add_edge(self, u: AdjacencyMatrixVertex, v: AdjacencyMatrixVertex, weight: int = 1) -> None:
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight

    def pp(self) -> None:
        # Print the top row
        print(" ".join([" ", *self.vertices.keys()]))
        # Print the vertex and weights
        for vertex, i in sorted(self.edge_indices.items()):
            print(" ".join([vertex, *list(map(str, self.edges[i]))]))


if __name__ == "__main__":
    # ug = AdjacencyListUndirectedGraph()
    # a = AdjacencyListVertex("A")
    # ug.add_vertex(a)
    # ug.add_vertex(AdjacencyListVertex("B"))
    # for i in range(ord("B"), ord("K")):
    #     ug.add_vertex(AdjacencyListVertex(chr(i)))
    # ug.pp()
    # print("*" * 100)

    # edges = ["AB", "AE", "BF", "CG", "DE", "DH", "EH", "FG", "FI", "FJ", "GJ", "IH"]
    # for edge in edges:
    #     ug.add_edge(edge[0], edge[1])
    # ug.pp()
    # print("*" * 100)

    ug = AdjacencyMatrixUndirectedGraph()
    a = AdjacencyMatrixVertex("A")
    ug.add_vertex(a)
    for i in range(ord("B"), ord("K")):
        ug.add_vertex(AdjacencyMatrixVertex(chr(i)))
    ug.pp()
    print("*" * 100)

    edges = ["AB", "AE", "BF", "CG", "DE", "DH", "EH", "FG", "FI", "FJ", "GJ", "IH"]
    for edge in edges:
        ug.add_edge(edge[0], edge[1])
    ug.pp()
