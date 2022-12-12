from __future__ import annotations

import sys
from typing import Union

HEAP_ITEM = Union[int, float]


class MaxHeap:
    def __init__(self, items: list[HEAP_ITEM]) -> None:
        # The heap is initialized with 0 as the 1st element
        # as it makes it easy to search for an element's parent
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self._float_up(len(self.heap) - 1)

    def __repr__(self) -> str:
        return str(self.heap[1:])

    def push(self, item: HEAP_ITEM) -> None:
        self.heap.append(item)
        self._float_up(len(self.heap) - 1)

    def peek(self) -> HEAP_ITEM | None:
        if len(self.heap) > 1:
            return self.heap[1]

    def pop(self) -> HEAP_ITEM | None:
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) - 1)
            max_item = self.heap.pop()
            self._bubble_down(1)
            return max_item
        elif len(self.heap) == 2:
            return self.heap.pop()

    def _float_up(self, idx: int) -> None:
        # This method re-arranges the element corresponding to the given index
        # so that it is in it's correct position in the heap
        if idx <= 1:
            return
        parent_index = idx // 2
        parent_item = self.heap[parent_index]
        current_item = self.heap[idx]
        if current_item > parent_item:
            self._swap(idx, parent_index)
            self._float_up(parent_index)

    def _bubble_down(self, idx: int) -> None:
        left_index = idx * 2
        right_index = left_index + 1
        largest_index = idx

        if len(self.heap) > left_index and self.heap[largest_index] < self.heap[left_index]:
            largest_index = left_index
        if len(self.heap) > right_index and self.heap[largest_index] < self.heap[right_index]:
            largest_index = right_index
        if largest_index != idx:
            self._swap(idx, largest_index)
            self._bubble_down(largest_index)

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class MinHeap:
    def __init__(self, items: list[HEAP_ITEM]) -> None:
        self.heap = [sys.maxsize]
        for item in items:
            self.heap.append(item)
            self._float_up(len(self.heap) - 1)

    def __repr__(self) -> str:
        return str(self.heap[1:])

    def push(self, item: HEAP_ITEM) -> None:
        self.heap.append(item)
        self._float_up(len(self.heap) - 1)

    def peek(self) -> HEAP_ITEM | None:
        if len(self.heap) > 1:
            return self.heap[1]

    def pop(self) -> HEAP_ITEM | None:
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) - 1)
            min_value = self.heap.pop()
            self._bubble_down(1)
            return min_value
        elif len(self.heap) == 2:
            return self.heap.pop()

    def _float_up(self, idx: int) -> None:
        if idx <= 1:
            return
        parent_index = idx // 2
        parent_item = self.heap[parent_index]
        current_item = self.heap[idx]
        if current_item < parent_item:
            self._swap(idx, parent_index)
            self._float_up(parent_index)

    def _bubble_down(self, idx: int) -> None:
        left_index = idx * 2
        right_index = left_index + 1
        largest_index = idx

        if len(self.heap) > left_index and self.heap[idx] > self.heap[left_index]:
            largest_index = left_index
        if len(self.heap) > right_index and self.heap[idx] > self.heap[right_index]:
            largest_index = right_index
        if largest_index != idx:
            self._swap(idx, largest_index)
            self._bubble_down(largest_index)

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == "__main__":
    nums = [95, 3, 21]
    maxhp = MaxHeap(nums)
    print(maxhp)
    maxhp.push(10)
    print(maxhp)
    maxhp.pop()
    print(maxhp)
    print("*" * 100)

    nums = [95, 3, 21]
    minhp = MinHeap(nums)
    print(minhp)
    minhp.push(10)
    print(minhp)
    minhp.pop()
    print(minhp)
