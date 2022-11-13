from __future__ import annotations

from typing import Any


class BinaryTree:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data: Any) -> None:
        # Removes duplicates
        if self.data == data:
            return

        # Left subtree
        if data < self.data:
            # Check left node first
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BinaryTree(data)
        else:
            # Right subtree
            if self.right:
                self.right.add_node(data)
            else:
                self.right = BinaryTree(data)

    def in_order_traversal(self) -> list[Any]:
        # Depth First Search technique
        elements = []

        # Left -> Base -> Right
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, value: Any) -> bool:
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
        return False

    def find_min(self) -> Any:
        # sorted_elements = self.in_order_traversal()
        # return min(sorted_elements)
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self) -> Any:
        # sorted_elements = self.in_order_traversal()
        # return max(sorted_elements)
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self) -> int:
        return sum(self.in_order_traversal())

    def pre_order_traversal(self) -> list[Any]:
        # Depth First Search technique
        # Starts with root then left sub tree and then right sub tree
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self) -> list[Any]:
        # Depth First Search technique
        # Starts with left, then right and last value is node
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def delete(self, value: Any) -> BinaryTree | None:
        if self.data is None:
            return

        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Node to be deleted has no sub-nodes
            if self.left is None and self.right is None:
                return
            # Node to be deleted has one sub-node
            elif self.left is None:
                return self.right
            # Node to be deleted has one sub-node
            elif self.right is None:
                return self.left
            else:
                # Node to be deleted has two sub-nodes
                min_value = self.right.find_min()
                self.data = min_value
                self.right = self.right.delete(min_value)
        return self


def build_tree(elements: list[Any]) -> BinaryTree:
    root = BinaryTree(elements[0])
    for num in elements[1:]:
        root.add_node(num)
    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(f"root node = {numbers_tree.data}")
    print(f"{numbers_tree.in_order_traversal() = }")
    print(f"{numbers_tree.search(9) = }")
    print(f"{numbers_tree.search(45) = }")
    print(f"{numbers_tree.find_min() = }")
    print(f"{numbers_tree.find_max() = }")
    print(f"{numbers_tree.calculate_sum() = }")
    print(f"{numbers_tree.pre_order_traversal() = }")
    print(f"{numbers_tree.post_order_traversal() = }")
    print(f"{numbers_tree.delete(1) = }")
    print(f"{numbers_tree.in_order_traversal() = }")
    print(f"{numbers_tree.delete(17) = }")
    print(f"{numbers_tree.in_order_traversal() = }")
