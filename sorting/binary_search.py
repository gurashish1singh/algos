from __future__ import annotations


def binary_search(arr: list[int], num_to_find: int) -> int:
    # Assumes list is sorted!
    # Time complexity: O(logn)
    # Space complexity: O(1)

    if not arr:
        return -1
    elif num_to_find == arr[0]:
        return 0
    elif num_to_find == arr[-1]:
        return len(arr) - 1
    else:
        length = len(arr)
        left_index = 0
        right_index = length - 1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_number = arr[middle_index]
            if num_to_find == middle_number:
                return middle_index
            elif num_to_find < middle_number:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
    return -1


def recursive_binary_search(
    arr: list[int], num_to_find: int, left_index: int, right_index: int
) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(logn)
    if right_index < left_index:
        return -1

    if num_to_find == arr[0]:
        return 0
    elif num_to_find == arr[-1]:
        return len(arr) - 1
    else:
        middle_index = (left_index + right_index) // 2
        middle_number = arr[middle_index]
        if num_to_find == middle_number:
            return middle_index
        elif num_to_find < middle_number:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

        return recursive_binary_search(arr, num_to_find, left_index, right_index)


def find_all_occurances(arr: list[int], num_to_find: int) -> list[int]:
    indexes = []
    times = arr.count(num_to_find)
    index = binary_search(arr, num_to_find)
    indexes.append(index)
    for i in range(1, times):
        if arr[index - i] == num_to_find:
            indexes.append(index - i)
        if arr[index + i] == num_to_find:
            indexes.append(index + i)
    return sorted(indexes)


if __name__ == "__main__":
    # nums = list(range(999))
    # iters = (
    #     (0, 0),
    #     (998, 998),
    #     (45, 45),
    #     (1, 1),
    #     (23213, -1),
    # )
    # for num, expected in iters:
    #     index = binary_search(nums, num)
    #     print(f"binary_search: {index = }")
    #     assert index == expected, f"{index = } not equal to {expected = }"
    #     index = recursive_binary_search(nums, num, 0, len(nums) - 1)
    #     print(f"recursive_binary_search: {index = }")
    #     assert index == expected, f"{index = } not equal to {expected = }"

    nums = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    iters = (
        (15, [5, 6, 7]),
        (34, [10, 11]),
        (1, [0]),
    )
    for num, expected in iters:
        indexes = find_all_occurances(nums, num)
        print(f"{indexes = }")
        assert indexes == expected, f"{indexes = } not equal to {expected = }"
