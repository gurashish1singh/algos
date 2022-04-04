from collections import namedtuple
from typing import Any, Union



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
        print(hash_idx)
        # This loop overwrited an existing key in the hash map
        for i, saved_tuple in enumerate(self._hash_array[hash_idx]):
            if len(saved_tuple) == 2 and key == saved_tuple[0]:
                self._hash_array[hash_idx][i] = (key, value)
                key_found = True
                break

        # This logic avoids collision of values while inserting them in a same hash index
        if not key_found:
            self._hash_array[hash_idx].append((key, value))

    def __getitem__(self, key: Union[int, str]) -> Any:
        idx = self.get_hash(key)
        for saved_tuple in self._hash_array[idx]:
            if key == saved_tuple[0]:
                return saved_tuple[1]

    def __delitem__(self, key: Union[int, str]) -> None:
        hash_idx = self.get_hash(key)
        for i, saved_tuple in enumerate(self._hash_array[hash_idx]):
            if key == saved_tuple[0]:
                del self._hash_array[hash_idx][i]

    def get_hash(self, key: Union[int, str]) -> int:
        hash_index = 0
        _key = str(key)
        for element in _key:
            hash_index += ord(element)
        return hash_index % self._max_size


class BasicLPHashMap():

    MAX_SIZE = 10
    KEY_VALUE_PAIR = namedtuple("key_value_pair", "key, value")

    def __init__(self) -> None:
        self._hash_array = [None] * self.MAX_SIZE

    def __setitem__(self, key: Union[int, str], value: Any) -> None:
        hash_idx = self.get_hash(key)
        actual_hash_idx = self.linear_probe_add(hash_idx)
        self._hash_array[actual_hash_idx] = self.KEY_VALUE_PAIR(key=key, value=value)

    def __getitem__(self, key: Union[int, str]) -> Any:
        hash_idx = self.get_hash(key)

        if self._hash_array[hash_idx].key == key:
            return self._hash_array[hash_idx]
        else:
            actual_hash_idx = self.linear_probe_get(hash_idx, key)
            return self._hash_array[actual_hash_idx]

    def linear_probe_add(self, hash_idx: int) -> int:
        # Linear probing method
        if hash_idx == self.MAX_SIZE - 1:
            hash_idx = 0

        try:
            while self._hash_array[hash_idx] is not None:
                hash_idx += 1
        except IndexError:
            raise Exception("Hash map is full")
        return hash_idx

    def linear_probe_get(self, hash_idx: int, key: Union[int, str]) -> int:
        # Linear probing method
        if hash_idx == self.MAX_SIZE - 1:
            hash_idx = 0

        try:
            while self._hash_array[hash_idx].key != key:
                hash_idx += 1
        except IndexError:
            raise Exception("Hash map is full")
        return hash_idx

    def __delitem__(self, key: Union[int, str]) -> None:
        hash_idx = self.get_hash(key)
        del self._hash_array[hash_idx]

    def get_hash(self, key: Union[int, str]) -> int:
        hash_index = 0
        _key = str(key)
        for element in _key:
            hash_index += ord(element)
        return hash_index % self.MAX_SIZE


if __name__ == "__main__":
    # b = BasicChainHashMap()
    b = BasicLPHashMap()
    print(b._hash_array)
    b["march 6"] = 2
    b["march 13"] = 3
    print(b._hash_array)
    b["march 17"] = 5
    print(b._hash_array)
    b["march 13"] = 34
    b["march 31"] = 45
    b["march 3"] = 78
    # b["march 7"] = 77
    # b["march 9"] = 55
    # b["march 19"] = 78
    # b["march 29"] = 22
    # b["march 28"] = 99
    print(b._hash_array)
    print(b["march 31"])
    print(b["march 13"])
    # del b["march 31"]
    # print(b._hash_array)
