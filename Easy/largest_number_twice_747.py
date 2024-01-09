from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_n = max(nums)

        for num in nums:
            if num != max_n and max_n < 2 * num:
                return -1

        return nums.index(max_n)


obj = Solution()
nums = [3, 6, 1, 0]
print(obj.dominantIndex(nums))
