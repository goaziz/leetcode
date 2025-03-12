from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = nums[i] % 2
        
        nums.sort()

        return nums
        