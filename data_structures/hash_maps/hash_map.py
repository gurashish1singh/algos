from __future__ import annotations

from collections import namedtuple
from typing import Any

HASH_PAIR = namedtuple("HASH_PAIR", "key, value")


class HashTable:
    def __init__(self) -> None:
        self.MAX_SIZE = 100
        self.hash_array = [None] * self.MAX_SIZE

    def get_hash_key(self, key: Any) -> int:
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.MAX_SIZE

    def __setitem__(self, key: Any, value: Any) -> None:
        h = self.get_hash_key(key)
        self.hash_array[h] = value

    def __getitem__(self, key: Any) -> Any | None:
        h = self.get_hash_key(key)
        return self.hash_array[h]

    def __delitem__(self, key: Any) -> None:
        h = self.get_hash_key(key)
        self.hash_array[h] = None


class ChainingHashTable:
    def __init__(self) -> None:
        self.MAX_SIZE = 100
        self.hash_array = [[] for _ in range(self.MAX_SIZE)]

    def get_hash_key(self, key: Any) -> int:
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.MAX_SIZE

    def __setitem__(self, key: Any, value: Any) -> None:
        h = self.get_hash_key(key)
        for item in self.hash_array[h]:
            if item and item.key == key:
                item.value = value
        else:
            self.hash_array[h].append(HASH_PAIR(key=key, value=value))

    def __getitem__(self, key: Any) -> Any | None:
        h = self.get_hash_key(key)
        for item in self.hash_array[h]:
            if item.key == key:
                return item.value

    def __delitem__(self, key: Any) -> None:
        h = self.get_hash_key(key)
        for item in self.hash_array[h]:
            if item.key == key:
                self.hash_array[h].remove(item)


class LinearProbingHashTable:
    def __init__(self) -> None:
        self.MAX_SIZE = 100
        self.hash_array = [None] * self.MAX_SIZE

    def get_hash_key(self, key: Any) -> int:
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.MAX_SIZE

    def __setitem__(self, key: Any, value: Any) -> None:
        h = self.get_hash_key(key)
        # This takes care of collision
        count = 0
        while self.hash_array[h]:
            h += 1
            count += 1
            if h == self.MAX_SIZE - 1:
                h = 0
            if count == self.MAX_SIZE:
                raise StopIteration("Hashmap is full")
        self.hash_array[h] = HASH_PAIR(key=key, value=value)

    def __getitem__(self, key: Any) -> Any | None:
        h = self.get_hash_key(key)
        while self.hash_array[h]:
            stored_pair = self.hash_array[h]
            if stored_pair.key == key:
                return stored_pair.value
            else:
                h += 1
                if h == self.MAX_SIZE - 1:
                    h = 0

    def __delitem__(self, key: Any) -> None:
        h = self.get_hash_key(key)
        while self.hash_array[h]:
            stored_pair = self.hash_array[h]
            if stored_pair.key == key:
                self.hash_array[h] = None
            else:
                h += 1
                if h == self.MAX_SIZE - 1:
                    h = 0


if __name__ == "__main__":
    ht = HashTable()
    ht["March 6"] = 130
    ht["March 7"] = 133
    ht["March 8"] = 131
    ht["March 9"] = 129
    ht["March 10"] = 132
    print(ht.hash_array)
    print(f"{ht['March 6'] = }")
    print(f"{ht['March 7'] = }")
    del ht["March 6"]
    print(f"{ht['March 6'] = }")
    # Collision
    ht["March 11"] = 135
    ht["March 20"] = 143
    print(f"{ht['March 11'] = }")
    print(f"{ht['March 20'] = }")
    print("*" * 190)

    cht = ChainingHashTable()
    cht["March 6"] = 130
    cht["March 7"] = 133
    cht["March 8"] = 131
    cht["March 9"] = 129
    cht["March 10"] = 132
    print(f"{cht['March 6'] = }")
    # Avoiding Collision
    cht["March 11"] = 135
    cht["March 20"] = 143
    print(cht.hash_array)
    print(f"{cht['March 11'] = }")
    print(f"{cht['March 20'] = }")
    del cht["March 6"]
    print(f"{cht['March 6'] = }")
    del cht["March 11"]
    print(cht.hash_array)
    print("*" * 190)

    lpht = LinearProbingHashTable()
    lpht["March 6"] = 130
    lpht["March 7"] = 133
    lpht["March 8"] = 131
    lpht["March 9"] = 129
    lpht["March 10"] = 132
    print(f"{lpht['March 6'] = }")
    print(f"{lpht['March 7'] = }")
    del lpht["March 6"]
    print(f"{lpht['March 6'] = }")
    # Collision
    lpht["March 11"] = 135
    lpht["March 20"] = 143
    print(f"{lpht['March 11'] = }")
    print(f"{lpht['March 20'] = }")
    print(lpht.hash_array)
    print("*" * 190)
