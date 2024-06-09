from collections import Counter
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:

        for i in range(len(arr) - 1):
            if arr[i: i + m] * k == arr[i: i + m * k]:
                return True

        return False


obj = Solution()
arr = [1, 2, 1, 2, 1, 1, 1, 3]
m = 2
k = 2
print(obj.containsPattern(arr, m, k))
