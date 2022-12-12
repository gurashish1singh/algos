from __future__ import annotations

from collections import deque
from typing import Any


class Queue:
    """
    A custom implementation of a queue
    """

    def __init__(self) -> None:
        self.buffer = deque()

    def __repr__(self) -> str:
        return str(self.buffer)

    def __len__(self) -> int:
        return len(self.buffer)

    def enqueue(self, value: Any) -> None:
        self.buffer.appendleft(value)

    def dequeue(self) -> Any:
        if self.empty:
            return "Buffer is empty."
        return self.buffer.pop()

    @property
    def empty(self) -> bool:
        return len(self.buffer) == 0

    @property
    def next_element(self) -> Any:
        return self.buffer[-1]


def binary_numbers(number: int = 1) -> None:
    # Returns all binary numbers uptil a given number
    number_queue = Queue()
    # By default the 1st number has been already inserted
    number_queue.enqueue(1)

    if number < 1:
        print(0)
        return

    for num, _ in enumerate(range(number), start=1):
        next_element = number_queue.next_element
        print(f"Binary representation for {num} is : {next_element}")
        # Enque items for the next 2 iterations, even if they are not used
        number_queue.enqueue(f"{next_element}0")
        number_queue.enqueue(f"{next_element}1")
        number_queue.dequeue()


if __name__ == "__main__":
    # a = Queue()
    # print(a)
    # a.enqueue({"first_item": 1})
    # a.enqueue({"second_item": 12})
    # a.enqueue({"third_item": 1123})
    # a.enqueue({"fourth_item": 431})
    # print(a.buffer)
    # print(a.dequeue())
    # print(a.dequeue())
    # print(a.dequeue())
    # print(len(a))

    binary_numbers(20)
