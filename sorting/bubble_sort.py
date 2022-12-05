from __future__ import annotations

from operator import itemgetter
from typing import (
    Any,
    Sequence,
)


def bubble_sort(arr: list[int]) -> list[int]:
    # Time complexity: O(n^2) (worst case) -> We have two loops
    # Space complexity: O(1) -> Using the same array
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort_with_key(seq: Sequence[Any], *, key: str) -> Sequence[Any]:
    # Time complexity: O(n^2) (worst case) -> We have two loops
    # Space complexity: O(1) -> Using the same array
    length = len(seq)
    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            if seq[j][key] > seq[j + 1][key]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                swapped = True
        if not swapped:
            break
    return seq


if __name__ == "__main__":
    # iters = (
    #     [5, 12, 2, 34, 67, 43, 1, 8, 54, 98, 10, 99],
    #     [1, 2, 3, 4, 5],
    #     ["beta", "alpha", "zulu", "gamma", "india"],
    # )
    # for arr in iters:
    #     expected = sorted(arr)
    #     ret = bubble_sort(arr)
    #     print(f"{ret = }")
    #     assert ret == expected, f"{ret = } is not the same as {expected = }"

    iters = (
        (
            [
                {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
                {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
                {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
                {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
            ],
            "transaction_amount",
        ),
        (
            [
                {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
                {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
                {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
                {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
            ],
            "name",
        ),
        (
            [
                {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
                {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
                {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
                {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
            ],
            "device",
        ),
    )
    for seq, key in iters:
        expected = sorted(seq, key=itemgetter(key))
        ret = bubble_sort_with_key(seq, key=key)
        print(f"{ret = }")
        assert ret == expected, f"{ret = } is not the same as {expected = }"
