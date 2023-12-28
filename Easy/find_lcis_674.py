from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1
        max_length = 1
        current_length = 1

        while left < right:
            if nums[left] < nums[left + 1]:
                current_length += 1
            else:
                current_length = 1

            left += 1
            max_length = max(max_length, current_length)

        return max_length

    def findLengthOfLCIS2(self, nums: List[int]) -> int:
        max_length = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 1

        return max_length


obj = Solution()
# nums = [1, 3, 5, 4, 7]
nums = [2, 2, 2, 2, 2]
print(obj.findLengthOfLCIS2(nums))
