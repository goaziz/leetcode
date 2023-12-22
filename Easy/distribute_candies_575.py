from collections import Counter
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        s = len(set(candyType))

        if s > n:
            return n
        return s


obj = Solution()
# print(obj.distributeCandies(candyType=[1, 1, 2, 3]))
# print(obj.distributeCandies(candyType=[1, 1, 2, 2, 3, 3]))
# print(obj.distributeCandies(candyType=[6, 6, 6, 6]))
print(obj.distributeCandies(candyType=[1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))
