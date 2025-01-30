from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i, val in enumerate(nums):
            if val > target:
                break

            if val == target:
                result.append(i)

        return result

    def targetIndices2(self, nums: List[int], target: int) -> List[int]:
        less_than_or_equal = 0
        less_than = 0

        for num in nums:
            if num <= target:
                less_than_or_equal += 1

            if num < target:
                less_than += 1

        return list(range(less_than, less_than_or_equal))


obj = Solution()
nums = [1, 2, 5, 2, 3]
target = 2
print(obj.targetIndices2(nums, target))
