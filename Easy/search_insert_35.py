import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums)
        low = 0

        while low < high:
            mid = (high - low) // 2 + low

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low


obj = Solution()
nums = [1, 3, 5, 6]
target = 0
print(bisect.bisect_left(nums, target))
print(obj.searchInsert(nums, target))
