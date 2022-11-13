from __future__ import annotations

from typing import Any


def merge_sort(arr: list[Any]) -> None:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    if len(arr) < 2:
        return

    mid = len(arr) // 2
    left_array = arr[:mid]
    right_array = arr[mid:]

    # We recursively called merge_sort to get the smallest possible arrays to sort
    merge_sort(left_array)
    merge_sort(right_array)
    merge_sorted_arrays(left_array, right_array, original_array=arr)


def merge_sorted_arrays(arr_1: list[Any], arr_2: list[Any], original_array: list[Any]) -> None:
    # To save on memory, we sort in place
    length_arr_1 = len(arr_1)
    length_arr_2 = len(arr_2)
    i = j = k = 0
    # Use both arrays so that we can stop when we reach the end of either array
    while i < length_arr_1 and j < length_arr_2:
        if arr_1[i] <= arr_2[j]:
            original_array[k] = arr_1[i]
            i += 1
        else:
            original_array[k] = arr_2[j]
            j += 1
        k += 1

    # After the shorter array has been exhausted, we append the remaining elements
    while i < length_arr_1:
        original_array[k] = arr_1[i]
        i += 1
        k += 1
    while j < length_arr_2:
        original_array[k] = arr_2[j]
        j += 1
        k += 1


if __name__ == "__main__":
    iters = (
        ([], []),
        ([2], [2]),
        ([3, 2], [2, 3]),
        ([10, 3, 15, 7, 8, 23, 98, 29], [3, 7, 8, 10, 15, 23, 29, 98]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        (["beta", "zulu", "alpha"], ["alpha", "beta", "zulu"]),
    )
    for nums, expected in iters:
        print(f"Before sorting: {nums = }")
        merge_sort(nums)
        print(f"After sorting: {nums = }")
        assert nums == expected, f"{nums = } is not the same as {expected = }"
        print("*" * 80)
