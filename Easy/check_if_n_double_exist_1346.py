from collections import Counter
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq = Counter(arr)

        for num in arr:
            m = 2 * num

            if m == 0 and freq.get(m) >= 2:
                return True
            if m in freq and m != 0:
                return True

        return False

    def checkIfExist2(self, arr: List[int]) -> bool:
        hashmap = {}

        for i, val in enumerate(arr):
            hashmap[val] = i

        for i, val in enumerate(arr):
            m = 2 * val

            if m in hashmap and hashmap[val] != i:
                return True

        return False
