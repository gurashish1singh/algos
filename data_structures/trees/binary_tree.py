from __future__ import annotations

from collections import deque
from typing import Any


class BinaryTree:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data: Any) -> None:
        # Remove duplicates
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BinaryTree(data)
        else:
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
        if value == self.data:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
        else:
            if self.right:
                return self.right.search(value)
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

    def level_order_traversal(self) -> list[Any]:
        # BFS
        queue = deque()
        elements = []
        if self.data is not None:
            queue.append(self)
            while queue:
                node = queue.popleft()
                elements.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
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
            # If we are at a leaf node
            if self.left is None and self.right is None:
                return
            # If we have one sub-child (left or right)
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                # We have two childs in the current node
                min_value = self.right.find_min()
                self.data = min_value
                self.right = self.right.delete(min_value)
        return self

    def get_height_dfs(self) -> int:
        if self.data is None:
            return 0

        left = right = 0
        if self.left:
            left = self.left.get_height_dfs()
        if self.right:
            right = self.right.get_height_dfs()
        return max(left, right) + 1

    def get_height_bfs(self) -> int:
        if self.data is None:
            return 0

        height = 0
        queue = deque()
        queue.append(self)
        while queue:
            # The current_size variable is used to count down the left and right nodes
            # the current node may have. We only increment the height when the current_size
            # reaches 0 i.e. we have parsed the left and right childs of the current node.
            current_size = len(queue)
            while current_size > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_size -= 1
            height += 1
        return height


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
    print(f"{numbers_tree.level_order_traversal() = }")
    print("*" * 100)

    numbers = [17, 4, 20]
    numbers_tree = build_tree(numbers)
    print(f"root node = {numbers_tree.data}")
    print(f"{numbers_tree.pre_order_traversal() = }")
    print(f"{numbers_tree.delete(4) = }")
    print(f"{numbers_tree.pre_order_traversal() = }")
    print(f"{numbers_tree.get_height_dfs() = }")
    print(f"{numbers_tree.get_height_bfs() = }")
