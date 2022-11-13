from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, data: Any = None, next_value: Any = None, prev_value: Any = None) -> None:
        self.data = data
        self.next_value = next_value
        self.prev_value = prev_value


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self) -> int:
        count = 0
        itr = self.head
        while itr:
            itr = itr.next_value
            count += 1
        return count

    def insert_at_beginning(self, data: Any) -> None:
        node = Node(data=data, next_value=self.head, prev_value=None)
        if self.head is None:
            self.head = node
        else:
            self.head.prev_value = node
            self.head = node

    def insert_at_end(self, data: Any) -> None:
        if self.head is None:
            self.insert_at_beginning(data=data)
        else:
            last_value = self.go_to_last_value()
            last_value.next_value = Node(data=data, next_value=None, prev_value=last_value)

    def insert_values(self, data: list[Any] | tuple[Any]) -> None:
        self.head = None
        for val in data:
            self.insert_at_end(val)

    def insert_value_at(self, index: int, value_to_insert: Any) -> None:
        if index < 0 or index >= len(self):
            raise IndexError(f"{index = } is out of range")

        if index == 0:
            self.insert_at_beginning(data=value_to_insert)
        else:
            current_index = 0
            itr = self.head
            while itr:
                if current_index == (index - 1):
                    node = Node(data=value_to_insert, next_value=itr.next_value, prev_value=itr)
                    itr.next_value.prev_value = node
                    itr.next_value = node
                    return
                itr = itr.next_value
                current_index += 1

    def insert_after_value(self, value_after: Any, value_to_insert: Any) -> None:
        itr = self.head
        while itr:
            if itr.data == value_after:
                node = Node(data=value_to_insert, next_value=itr.next_value, prev_value=itr)
                itr.next_value.prev_value = node
                itr.next_value = node
                return
            itr = itr.next_value

        raise ValueError(f"{value_after = } not found in the linked list")

    def remove_by_value(self, value_to_remove: Any) -> None:
        itr = self.head
        while itr:
            if itr.data == value_to_remove:
                itr.prev_value.next_value = itr.next_value
                itr.next_value.prev_value = itr.prev_value
                return
            itr = itr.next_value

        raise ValueError(f"{value_to_remove = } not found in the linked list")

    def pp(self, reverse: bool = False) -> None:
        dll_str = ""
        if reverse:
            itr = self.go_to_last_value()
            attribute = "prev_value"
        else:
            itr = self.head
            attribute = "next_value"

        while itr:
            sep = "<-->" if getattr(itr, attribute) else ""
            dll_str += f"{itr.data}{sep}"
            itr = getattr(itr, attribute)
        print(dll_str)

    def go_to_last_value(self) -> Node:
        itr = self.head
        while itr.next_value:
            itr = itr.next_value
        return itr


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert_at_beginning(4)
    dll.insert_at_beginning(5)
    dll.insert_at_beginning(2)
    dll.pp()
    dll.insert_at_end(34)
    dll.insert_at_end(112)
    dll.pp()
    dll.pp(reverse=True)
    print(f"{len(dll) = }")
    dll.insert_values([5, 6, 3, 2, 8, 11])
    dll.pp()
    print(f"{len(dll) = }")
    dll.insert_value_at(0, 23)
    dll.pp()
    dll.pp(reverse=True)
    dll.insert_value_at(2, 99)
    dll.pp()
    dll.pp(reverse=True)
    dll.insert_after_value(23, 123)
    dll.pp()
    dll.pp(reverse=True)
    dll.insert_after_value(123, 56)
    dll.pp()
    dll.pp(reverse=True)
    dll.remove_by_value(123)
    dll.pp()
    dll.pp(reverse=True)
