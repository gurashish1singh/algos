from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, data: Any = None, next_value: Any = None) -> None:
        self.data = data
        self.next_value = next_value


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next_value
        return count

    def insert_at_beginning(self, data: Any) -> None:
        # If we already have a head, we create a node who's
        # next value points to the current head. Then we assign the current
        # head as the new node.
        node = Node(data=data, next_value=self.head)
        self.head = node

    def insert_at_end(self, data: Any) -> None:
        if self.head is None:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        while itr.next_value:
            itr = itr.next_value

        # The last value will not have a next value
        itr.next_value = Node(data=data, next_value=None)

    def insert_values(self, data: list[Any] | tuple[Any]) -> None:
        # Blank out the whole linked list
        self.head = None
        for val in data:
            self.insert_at_end(val)

    def remove_at(self, index: int) -> None:
        if index < 0 or index >= len(self):
            raise IndexError(f"{index = } is out of range")

        if index == 0:
            self.head = self.head.next_value
            return

        current_index = 0
        itr = self.head
        while itr:
            # To remove the element at the given index, we need to stop at the previous element
            if current_index == (index - 1):
                itr.next_value = itr.next_value.next_value
                break
            itr = itr.next_value
            current_index += 1

    def insert_at(self, index: int, data: Any) -> None:
        if index < 0 or index > len(self):
            raise IndexError(f"Given {index = } is incorrect.")

        if index == 0:
            self.insert_at_beginning(data=data)
            return

        current_index = 0
        itr = self.head
        while itr:
            if current_index == (index - 1):
                itr.next_value = Node(data=data, next_value=itr.next_value)
                break
            itr = itr.next_value
            current_index += 1

    def insert_after_value(self, value_after: Any, value_to_insert: Any) -> None:
        itr = self.head
        while itr:
            if value_after == itr.data:
                itr.next_value = Node(data=value_to_insert, next_value=itr.next_value)
                return
            itr = itr.next_value

        raise ValueError(f"{value_after = } not found in the linked list")

    def remove_by_value(self, value_to_remove: Any) -> None:
        itr = self.head
        while itr:
            if value_to_remove == itr.next_value.data:
                itr.next_value = itr.next_value.next_value
                return
            itr = itr.next_value

        raise ValueError(f"{value_to_remove = } not found in the linked list")

    def pp(self) -> None:
        if self.head is None:
            print("Linked list is empty")
            return

        ll_str = ""
        itr = self.head
        while itr:
            sep = "-->" if itr.next_value else ""
            ll_str += f"{str(itr.data)}{sep}"
            itr = itr.next_value
        print(ll_str)


if __name__ == "__main__":
    ll = LinkedList()
    ll.pp()
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(3)
    ll.pp()
    ll.insert_at_end(11)
    ll.insert_at_end(22)
    ll.pp()
    ll.insert_values([1, 4, 6, 87, 34, 2])
    ll.pp()
    print(f"{len(ll) = }")
    ll.remove_at(4)
    ll.pp()
    print(f"{len(ll) = }")
    ll.insert_at(2, 33)
    ll.pp()
    ll.insert_at(4, 66)
    ll.pp()
    print(f"{len(ll) = }")
    ll.insert_after_value(1, 12)
    ll.pp()
    ll.insert_after_value(33, 34)
    ll.pp()
    ll.remove_by_value(34)
    ll.pp()
