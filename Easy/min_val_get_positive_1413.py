from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        total = 0

        for num in nums:
            total += num
            min_val = min(min_val, total)

        return 1 - min_val


obj = Solution()
nums = [-3, 2, -3, 4, 2]
print(obj.minStartValue(nums))
