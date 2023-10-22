from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        temp = nums[0]
        for i in range(len(nums)):
            if temp != nums[i]:
                temp = nums[i]
                count += 1
                nums[count] = temp

        return count + 1

    def removeDuplicates2(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]

        return count + 1


obj = Solution()
# nums = [1, 1, 2]
nums = [1, 1]
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(obj.removeDuplicates2(nums))
