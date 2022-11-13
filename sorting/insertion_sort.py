from __future__ import annotations


def insertion_sort(arr: list[int]) -> None:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    length = len(arr)
    if length < 2:
        return arr

    # Starting from the 2nd element as we assume that the 1st element is sorted
    for i in range(1, length):
        anchor = arr[i]
        prev = i - 1
        while prev >= 0 and anchor < arr[prev]:
            # We swap elements lower than anchor
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = anchor


if __name__ == "__main__":
    iters = (
        ([], []),
        ([2], [2]),
        ([3, 2], [2, 3]),
        ([3, 1, 2], [1, 2, 3]),
        ([11, 9, 29, 7, 2, 15, 28], [2, 7, 9, 11, 15, 28, 29]),
    )
    for nums, expected in iters:
        print(f"Before sorting: {nums = }")
        insertion_sort(nums)
        print(f"After sorting: {nums = }")
        assert nums == expected, f"{nums = } is not the same as {expected = }"
        print("*" * 80)
