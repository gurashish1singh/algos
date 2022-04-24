from collections import deque
from typing import Any


class BasicStack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, item: Any) -> None:
        self.container.append(item)

    def pop(self) -> Any:
        try:
            return self.container.pop()
        except IndexError:
            return "Container is empty"

    def peek(self) -> Any:
        try:
            return self.container[-1]
        except IndexError:
            return "Container is empty"

    def size(self) -> int:
        return len(self.container)

    @property
    def empty(self) -> bool:
        return len(self.container) == 0


def reverse_string(input_str: str) -> str:
    # A very basic implementation of reversing a string using stack
    stack = BasicStack()
    for item in input_str:
        stack.push(item)

    reversed = []
    while stack.empty is False:
        reversed.append(stack.pop())
    return "".join(reversed)


def is_bracket_balanced(input_str: str) -> bool:
    ACCEPTED_PARANS = {"{", "}", "(", ")", "[", "]"}
    PARANS_COMBO = {
        "}": "{",
        ")": "(",
        "]": "[",
    }

    stack = BasicStack()
    for item in input_str:
        stack.push(item)

    balanced = False
    matching_parans = None
    last_val = stack.pop()
    if last_val not in PARANS_COMBO:
        # This handles all case where the last character is not a parans
        return False
    else:
        matching_parans = last_val

    while stack.empty is False:
        item = stack.pop()
        if item in ACCEPTED_PARANS:
            if item == PARANS_COMBO[matching_parans]:
                balanced = True
            else:
                balanced = False
    return balanced


if __name__ == "__main__":
    # stack = deque()
    # stack.append("first_item")
    # print(stack)
    # stack.append("second_item")
    # stack.append("third_item")
    # stack.append("fourth_item")
    # print(stack)
    # print(stack.pop())
    # print(stack)

    # stack = BasicStack()
    # stack.push(5)
    # print(stack.peek())
    # print(stack.size())
    # print(stack.pop())
    # print(stack.empty)
    # print(stack.pop())
    # print(stack.peek())

    # print(reverse_string("This should be reversed!"))

    assert is_bracket_balanced("{'hello'}") is True
    assert is_bracket_balanced("{'hello'") is False
    assert is_bracket_balanced("[{'hello'}]") is True
    assert is_bracket_balanced("[{'hello'})") is False
    assert is_bracket_balanced("[a) + (b)") is False
    assert is_bracket_balanced("))((a+b}{") is False
