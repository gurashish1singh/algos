from __future__ import annotations

from typing import Any


class BasicStack:
    def __init__(self) -> None:
        self.container = []

    def __len__(self) -> int:
        return len(self.container)

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

    @property
    def empty(self) -> bool:
        return len(self.container) == 0


def reverse_string(input_str: str) -> str:
    # A very basic implementation of reversing a string using stack
    stack = BasicStack()
    for item in input_str:
        stack.push(item)

    reversed_str = []
    while stack.empty is False:
        reversed_str.append(stack.pop())
    return "".join(reversed_str)


def is_bracket_balanced(input_str: str) -> bool:
    PARANS_COMBO = {
        "}": "{",
        ")": "(",
        "]": "[",
    }
    OPENING_PARANS = set(PARANS_COMBO.values())
    CLOSING_PARANS = set(PARANS_COMBO.keys())

    stack = BasicStack()
    for char in input_str:
        if char in OPENING_PARANS:
            # We only push the opening brackets to stack
            stack.push(char)
        elif char in CLOSING_PARANS:
            if stack.empty:
                return False
            elif PARANS_COMBO.get(char) != stack.pop():
                # False is returned for any closing parans that doesnt have a matching
                # opening parans at thet top of the stack
                return False
    return stack.empty


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

    stack = BasicStack()
    stack.push(5)
    print(stack.peek())
    print(len(stack))
    print(stack.pop())
    print(stack.empty)
    print(stack.pop())
    print(stack.peek())

    print(reverse_string("This should be reversed!"))

    assert is_bracket_balanced("{'hello'}") is True
    assert is_bracket_balanced("{'hello'") is False
    assert is_bracket_balanced("[{'hello'}]") is True
    assert is_bracket_balanced("[{'hello'})") is False
    assert is_bracket_balanced("[a) + (b)") is False
    assert is_bracket_balanced("))((a+b}{") is False
    assert is_bracket_balanced("[a] + {b)") is False
    assert is_bracket_balanced(r"{a} + (b)") is True
