from __future__ import annotations

from collections import namedtuple
from typing import (
    Any,
    Union,
)


class BasicChainHashMap:

    # Better to have a prime number for max size
    MAX_SIZE = 101
    KEY_VALUE_PAIR = namedtuple("key_value_pair", "key, value")

    def __init__(self) -> None:
        # Not optimized hash map. The most basic map there can be
        # List of list will help against collision
        self._hash_array = [[] for i in range(self.MAX_SIZE)]

    def __setitem__(self, key: Union[int, str], value: Any) -> None:
        key_found = False
        hash_idx = self.get_hash(key)

        # This loop overwrites an existing key in the hash map
        for i, key_value_pair in enumerate(self._hash_array[hash_idx]):
            if len(key_value_pair) == 2 and key == key_value_pair.key:
                self._hash_array[hash_idx][i] = self.KEY_VALUE_PAIR(key=key, value=value)
                key_found = True
                break

        # This logic avoids collision of values while inserting them in a same hash index
        if not key_found:
            self._hash_array[hash_idx].append(self.KEY_VALUE_PAIR(key=key, value=value))

    def __getitem__(self, key: Union[int, str]) -> Any:
        idx = self.get_hash(key)
        for key_value_pair in self._hash_array[idx]:
            if key == key_value_pair.key:
                return key_value_pair.value
        raise KeyError(f"The {key = } does not exist in the hash map!")

    def __delitem__(self, key: Union[int, str]) -> None:
        hash_idx = self.get_hash(key)
        for i, key_value_pair in enumerate(self._hash_array[hash_idx]):
            if key == key_value_pair.key:
                del self._hash_array[hash_idx][i]
        raise KeyError(f"The {key = } does not exist in the hash map!")

    def get_hash(self, key: Union[int, str]) -> int:
        hash_index = 0
        _key = str(key)
        for element in _key:
            hash_index += ord(element)
        return hash_index % self.MAX_SIZE


class BasicLinearProbingHashMap:
    """
    This method iteratively finds the immediate next empty location to insert a given value
    """

    MAX_SIZE = 10
    KEY_VALUE_PAIR = namedtuple("key_value_pair", "key, value")

    def __init__(self) -> None:
        self._hash_array = [None] * self.MAX_SIZE

    def __setitem__(self, key: Union[int, str], value: Any) -> None:
        hash_idx = self.get_hash(key)
        if self._hash_array[hash_idx] and self._hash_array[hash_idx].key == key:
            # Overwriting the value of an existing key
            self._hash_array[hash_idx] = self.KEY_VALUE_PAIR(key=key, value=value)
        else:
            actual_hash_idx = self.add_value(hash_idx)
            self._hash_array[actual_hash_idx] = self.KEY_VALUE_PAIR(key=key, value=value)

    def add_value(self, hash_idx: int) -> int:
        # This method returns the index of a free location to store a given value in
        if hash_idx == self.MAX_SIZE - 1:
            hash_idx = 0

        try:
            while self._hash_array[hash_idx] is not None:
                hash_idx += 1
        except IndexError:
            raise Exception("Hash map is full")
        return hash_idx

    def __getitem__(self, key: Union[int, str]) -> Any:
        hash_idx = self.get_hash(key)

        if self._hash_array[hash_idx].key == key:
            return self._hash_array[hash_idx]
        else:
            actual_hash_idx = self.get_value(hash_idx, key)
            return self._hash_array[actual_hash_idx]

    def __delitem__(self, key: Union[int, str]) -> None:
        hash_idx = self.get_hash(key)
        if self._hash_array[hash_idx].key == key:
            self._hash_array[hash_idx] = None
        else:
            actual_hash_idx = self.get_value(hash_idx, key)
            self._hash_array[actual_hash_idx] = None

    def get_value(self, hash_idx: int, key: Union[int, str]) -> int:
        # This method returns the index of the matching key
        for idx in self.get_linear_probe_range(hash_idx):
            if self._hash_array[idx] and self._hash_array[idx].key == key:
                return idx
        raise KeyError(f"The {key = } does not exist in the hash map!")

    def get_linear_probe_range(self, hash_idx: int) -> list[int]:
        # Returns a list for idx = 7 as:
        # [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
        return [*range(hash_idx, self.MAX_SIZE)] + [*range(0, hash_idx)]

    def get_hash(self, key: Union[int, str]) -> int:
        hash_index = 0
        _key = str(key)
        for element in _key:
            hash_index += ord(element)
        return hash_index % self.MAX_SIZE


if __name__ == "__main__":
    # b = BasicChainHashMap()
    b = BasicLinearProbingHashMap()
    print(b._hash_array)
    b["march 6"] = 2
    b["march 13"] = 3
    print(b._hash_array)
    b["march 17"] = 5
    print(b._hash_array)
    b["march 13"] = 34
    b["march 31"] = 45
    b["march 3"] = 78
    b["march 7"] = 77
    b["march 9"] = 55
    b["march 19"] = 78
    b["march 29"] = 22
    # b["march 28"] = 99
    print(b._hash_array)
    print(b["march 31"])
    print(b["march 13"])
    del b["march 31"]
    print(b._hash_array)
    # del b["march 32"]
    print(b["march 32"])
