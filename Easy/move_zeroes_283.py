from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1
        print(nums)


obj = Solution()
nums = [0, 1, 0, 3, 12]
print(obj.moveZeroes(nums))
