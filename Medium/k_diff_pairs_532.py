from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        freq = Counter(nums)

        if k == 0:
            for num in freq:
                if freq[num] > 1:
                    count += 1
        else:
            for num in freq:
                if num + k in freq:
                    count += 1

        return count


obj = Solution()
nums = [3, 1, 4, 1, 5]
k = 2
print(obj.findPairs(nums, k))
