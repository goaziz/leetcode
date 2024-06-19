from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.hashmap = {}
        self.count = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hashmap[idKey] = value
        result = []

        while self.count in self.hashmap:
            result.append(self.hashmap[self.count])
            self.count += 1

        return result
