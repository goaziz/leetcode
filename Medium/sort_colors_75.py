from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            elif num == 2:
                twos += 1

        for i in range(len(nums)):
            if zeros != 0:
                nums[i] = 0
                zeros -= 1
            elif ones != 0:
                nums[i] = 1
                ones -= 1
            elif twos != 0:
                nums[i] = 2
                twos -= 1

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = j = 0
        n = len(nums) - 1

        while j <= n:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            else:
                j += 1

        return nums

    def sortColors3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_map = {0: 0, 1: 0, 2: 0}

        for num in nums:
            count_map[num] += 1

        idx = 0
        for i in range(3):
            while count_map[i] > 0:
                nums[idx] = i
                idx += 1
                count_map[i] -= 1

        return nums


obj = Solution()
nums = [2, 0, 1, 2, 0, 1, 0, 2, 2, 0, 2, 1, 1, 0]
print(obj.sortColors2(nums))
