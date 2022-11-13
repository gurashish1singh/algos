from __future__ import annotations

from typing import Any


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


if __name__ == "__main__":
    t = HashTable()
    t["March 6"] = 130
    t["March 7"] = 133
    t["March 8"] = 131
    t["March 9"] = 129
    t["March 10"] = 132
    print(t.hash_array)
    print(f"{t['March 6'] = }")
    print(f"{t['March 7'] = }")
    del t["March 6"]
    print(f"{t['March 6'] = }")
