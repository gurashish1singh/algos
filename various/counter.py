from typing import Any


class Counter:
    """
    A custom implementation of collections.Counter
    """

    def __init__(self, iterable_item: str = "") -> None:
        if isinstance(iterable_item, str):
            self.iterable_item = iterable_item
        else:
            raise RuntimeError(f"For now {__class__.__name__} class only accepts strings")
        self.container = {}
        self.__count_objects()

    def __count_objects(self) -> None:
        for item in self.iterable_item:
            if item in self.container:
                self.container[item] += 1
            else:
                self.container[item] = 1

    def __repr__(self) -> str:
        return f"Counter({self.container})"

    def items(self) -> list[tuple[str, Any]]:
        return [*self.container.items()]

    def keys(self) -> list[str]:
        return [*self.container.keys()]

    def values(self) -> list[Any]:
        return [*self.container.values()]

    def most_common(self, max_items: int = 0) -> list[tuple[str, Any]]:
        common_items = sorted(self.container.items(), key=lambda item: item[1], reverse=True)
        if max_items > 0:
            return common_items[slice(max_items)]
        return common_items


if __name__ == "__main__":
    c = Counter("bbaaacccassjjj")
    print(c)
    print(c.items())
    print(c.keys())
    print(c.values())
    print(c.most_common())
    print(c.most_common(1))
    print(c.most_common(2))
