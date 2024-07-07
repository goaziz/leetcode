from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        max_sum_so_far = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            max_sum_so_far = max(max_sum_so_far, current_max)

        return max_sum_so_far

    def maxSubArray2(self, nums: List[int]) -> int:
        max_subarray = 0
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray


obj = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(obj.maxSubArray2(nums))
