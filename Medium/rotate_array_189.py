from typing import List


class Solution:

    def reverse(self, i, j, nums):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        self.reverse(0, j, nums)
        self.reverse(0, k - 1, nums)
        self.reverse(k, j, nums)


obj = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(obj.rotate(nums, k))
