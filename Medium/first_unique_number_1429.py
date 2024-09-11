from collections import Counter
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.freq = Counter(nums)

    def showFirstUnique(self) -> int:
        for key, val in self.freq.items():
            if val == 1:
                return key

        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.freq[value] = self.freq.get(value, 0) + 1
