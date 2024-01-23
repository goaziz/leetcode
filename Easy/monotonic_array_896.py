from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing = True

            if nums[i] < nums[i - 1]:
                decreasing = True

            if increasing and decreasing:
                return False

        return True

    def isMonotonic2(self, nums: List[int]) -> bool:
        increasing = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
        decreasing = all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))

        return increasing or decreasing

    def isMonotonic3(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False

            if nums[i] < nums[i + 1]:
                decreasing = False

        return increasing or decreasing


obj = Solution()
# nums = [1, 2, 2, 3]
# nums = [6, 5, 4, 4]
nums = [1, 3, 2]
print(obj.isMonotonic(nums))
