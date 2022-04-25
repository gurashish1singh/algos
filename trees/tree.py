from typing import Any


class TreeNode:
    """
    A basic tree data structure implementation
    """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def __repr__(self) -> str:
        return f"Tree(data={self.data}, parent={self.parent})"

    def add_child(self, child) -> None:
        # The child has a parent property set as it is being
        # added to the 'children' list
        child.parent = self
        self.children.append(child)

    def pretty_print(self) -> None:
        spaces = " " * self.get_number_of_parents() * 2
        prefix = f"{spaces}|-" if self.parent else ""
        print(f"{prefix}{self.data}")
        for child in self.children:
            child.pretty_print()

    def get_number_of_parents(self) -> int:
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


def build_product_tree() -> TreeNode:
    root = TreeNode("Trees")

    apple = TreeNode("Apple")
    apple.add_child(TreeNode("Red Apple"))
    apple.add_child(TreeNode("Green Apple"))

    orange = TreeNode("Orange")
    orange.add_child(TreeNode("Mandarin"))
    orange.add_child(TreeNode("Clementine"))

    root.add_child(apple)
    root.add_child(orange)
    return root


if __name__ == "__main__":
    root = build_product_tree()
    print(root)
    root.pretty_print()
