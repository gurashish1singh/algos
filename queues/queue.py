from collections import deque
from typing import Any


class Queue:
    """
    A custom implementation of a queue
    """

    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, value: Any) -> None:
        self.buffer.appendleft(value)

    def dequeue(self) -> Any:
        if self.empty:
            return "Buffer is empty."
        return self.buffer.pop()

    @property
    def empty(self) -> bool:
        return len(self.buffer) == 0

    def size(self) -> int:
        return len(self.buffer)

    def next_element(self) -> Any:
        return self.buffer[-1]


def binary_numbers(numbers: int = 1) -> None:
    number_queue = Queue()
    # By default the 1st number has been already inserted
    number_queue.enqueue(1)

    if numbers < 1:
        print(0)
        return

    for _ in range(numbers):
        next_element = number_queue.next_element()
        print(next_element)
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
    # print(a.size())

    binary_numbers(20)
