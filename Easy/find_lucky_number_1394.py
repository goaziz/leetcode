from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = Counter(arr)

        max_n = -1
        for key, val in hashmap.items():
            if key == val:
                max_n = max(max_n, val)

        return max_n


obj = Solution()
arr = [2, 2, 2, 3, 3]
print(obj.findLucky(arr))
