from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for idx, val in enumerate(nums):
            if left_sum == total - left_sum - val:
                return idx

            left_sum += val

        return -1


obj = Solution()
nums = [-1, -1, 0, 1, 1, 0]
print(obj.pivotIndex(nums))
