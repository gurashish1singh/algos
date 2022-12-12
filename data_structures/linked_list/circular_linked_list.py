from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, data: Any = None, next_value: Any = None) -> None:
        self.data = data
        self.next_value = next_value


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def insert_after_root(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data=data)
            self.head.next_value = self.head
        else:
            node = Node(data=data, next_value=self.head.next_value)
            self.head.next_value = node
        self.size += 1

    def pp(self) -> None:
        if self.head is None:
            print("Linked list is empty")
            return

        ll_str = []
        count = 0
        itr = self.head
        while count < self.size:
            sep = "-->" if itr.next_value else ""
            ll_str.append(f"{str(itr.data)}{sep}")
            itr = itr.next_value
            count += 1
        print("".join(ll_str))


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.pp()
    cll.insert_after_root(5)
    cll.pp()
    cll.insert_after_root(34)
    cll.pp()
    print(f"{len(cll) = }")
