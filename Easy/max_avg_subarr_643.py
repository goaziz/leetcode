from cmath import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -inf

        for i in range(len(nums)):
            sub_arr = nums[i:i + k]
            if len(sub_arr) == k:
                val = sum(sub_arr) / k
                max_avg = max(max_avg, val)

        return max_avg

    # better solution
    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        cur = result = sum(nums[0: k])
        for i in range(len(nums) - k):
            cur += nums[i + k] - nums[i]
            result = max(cur, result)
        return float(result) / k


obj = Solution()
nums = [0]
k = 1
print(obj.findMaxAverage(nums, k))
