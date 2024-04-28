from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        n = len(arr)
        ans = 0
        for key, val in c.items():
            percent = (val / n) * 100

            if percent > 25:
                ans = key

        return ans

    def findSpecialInteger2(self, arr: List[int]) -> int:
        hashmap = {}
        target = len(arr) / 4

        for i in arr:
            hashmap[i] += 1
            if hashmap[i] > target:
                return i

        return -1

    def findSpecialInteger2(self, arr: List[int]) -> int:
        size = len(arr) // 4
        for i in range(len(arr) - size):
            if arr[i] == arr[i + size]:
                return arr[i]

        return -1


obj = Solution()
arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
print(obj.findSpecialInteger2(arr))
