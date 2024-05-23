from collections import Counter
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashmap = Counter(arr)
        count = 0

        for num in arr:
            n = num + 1
            if n in hashmap:
                count += 1

        return count


obj = Solution()
arr = [1, 1, 3, 3, 5, 5, 7, 7]
print(obj.countElements(arr))
