from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) > len(arr):
            return False

        c1 = Counter(target)
        c2 = Counter(arr)

        return c1 == c2


obj = Solution()
target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(obj.canBeEqual(target, arr))
