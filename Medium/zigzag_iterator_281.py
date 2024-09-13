from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.v1_index = 0
        self.v2_index = 0
        self.turn = 0

    def next(self) -> int:
        if self.hasNext():
            if self.turn == 0 and self.v1_index < len(self.v1) or self.v2_index >= len(self.v2):
                val = self.v1[self.v1_index]
                self.v1_index += 1
                self.turn = 1
            else:
                val = self.v2[self.v2_index]
                self.v2_index += 1
                self.turn = 0

            return val

    def hasNext(self) -> bool:
        return self.v1_index < len(self.v1) or self.v2_index < len(self.v2)
