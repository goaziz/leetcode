from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            min_n = float('inf')
            max_n = float('-inf')
            for j in range(i, len(nums)):
                min_n = min(min_n, nums[i], nums[j])
                max_n = max(max_n, nums[i], nums[j])
                ans += max_n - min_n

        return ans


obj = Solution()
nums = [4, -2, -3, 4, 1]
print(obj.subArrayRanges(nums))
