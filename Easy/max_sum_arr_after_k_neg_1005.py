from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= -1

        return sum(nums)


obj = Solution()
nums = [2, -3, -1, 5, -4]
k = 2
print(obj.largestSumAfterKNegations(nums, k))
