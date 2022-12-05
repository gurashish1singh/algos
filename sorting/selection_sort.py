from __future__ import annotations

from typing import Any


def selection_sort(arr: list[Any]) -> None:
    # Time complexity: O(n^2)
    length = len(arr)
    if length < 2:
        return arr

    for i in range(length - 1):
        min_index = i
        for j in range(min_index + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    iters = (
        ([], []),
        ([2], [2]),
        ([5, 3, 2], [2, 3, 5]),
        ([78, 12, 15, 8, 61, 54, 23, 27], [8, 12, 15, 23, 27, 54, 61, 78]),
    )
    for nums, expected in iters:
        print(f"Before sorting: {nums = }")
        selection_sort(nums)
        print(f"After sorting: {nums = }")
        assert nums == expected, f"{nums = } is not the same as {expected = }"
        print("*" * 80)
