from __future__ import annotations

from typing import Any


class Node:
    """
    A basic tree data structure implementation
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.sub_nodes = []
        self.parent = None

    def __repr__(self) -> str:
        return f"Tree(data={self.data}, parent={self.parent})"

    def add_sub_node(self, sub_node: Any) -> None:
        # The sub_node has a parent property set as it is being
        # added to the 'sub_nodes' list
        sub_node.parent = self
        self.sub_nodes.append(sub_node)

    def pretty_print(self) -> None:
        spaces = " " * self.get_number_of_parents() * 2
        prefix = f"{spaces}|-" if self.parent else ""
        print(f"{prefix}{self.data}")
        for sub_node in self.sub_nodes:
            sub_node.pretty_print()

    def get_number_of_parents(self) -> int:
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


def build_product_tree() -> Node:
    main_tree = Node("Trees")

    apple = Node("Mango")
    apple.add_sub_node(Node("Honey"))
    apple.add_sub_node(Node("Kent"))

    orange = Node("Orange")
    orange.add_sub_node(Node("Mandarin"))
    orange.add_sub_node(Node("Clementine"))

    main_tree.add_sub_node(apple)
    main_tree.add_sub_node(orange)
    return main_tree


if __name__ == "__main__":
    main_tree = build_product_tree()
    print(main_tree)
    main_tree.pretty_print()
