from __future__ import annotations

from typing import Any


def shell_sort(arr: list[Any]) -> list[Any]:
    # Time complexity: O(n^2)
    # Space complexity: O
    # Idea is to divide the array by n/2 and sort the sub-array and repeat
    # until the gap is down to 1 (at which point this becomes the same as insertion sort)
    length = len(arr)
    gap = length // 2

    # We start with element at gap index and compare against "current index - gap" element
    while gap > 0:
        indexes_to_delete = set()
        for i in range(gap, length):
            anchor = arr[i]
            prev_index = i
            while prev_index >= gap and arr[prev_index - gap] >= anchor:
                if anchor == arr[prev_index - gap]:
                    indexes_to_delete.add(prev_index)
                arr[prev_index] = arr[prev_index - gap]
                prev_index -= gap
            arr[prev_index] = anchor

        # Deleting duplicates
        if indexes_to_delete:
            indexes_to_delete = reversed(sorted(list(indexes_to_delete)))
            for index in indexes_to_delete:
                del arr[index]
        # Since we are deleting after the loop, length changes for next iteration
        gap = gap // 2
        length = len(arr)


if __name__ == "__main__":
    iters = (
        ([], []),
        ([2], [2]),
        ([5, 3, 2], [2, 3, 5]),
        ([21, 38, 29, 17, 4, 25, 11, 32, 9], [4, 9, 11, 17, 21, 25, 29, 32, 38]),
        ([2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3], [0, 1, 2, 3, 5, 7, 8, 9]),
    )
    for nums, expected in iters:
        print(f"Before sorting: {nums = }")
        shell_sort(nums)
        print(f"After sorting: {nums = }")
        assert nums == expected, f"{nums = } is not the same as {expected = }"
        print("*" * 80)
