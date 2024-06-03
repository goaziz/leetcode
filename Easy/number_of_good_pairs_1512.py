from collections import Counter, defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        count = 0

        for num, cnt in c.items():
            n = (cnt * (cnt - 1)) // 2
            count += n

        return count

    def numIdenticalPairs2(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        count = 0

        for num in nums:
            count += counts[num]
            counts[num] += 1

        return count


obj = Solution()
nums = [1, 1, 1, 1]
print(obj.numIdenticalPairs2(nums))
