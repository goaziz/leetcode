from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for idx, val in zip(index, nums):
            target.insert(idx, val)

        return target

    def createTargetArray2(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in range(len(nums)):
            target.insert(index[i], nums[i])

        return target


obj = Solution()
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print(obj.createTargetArray2(nums, index))
