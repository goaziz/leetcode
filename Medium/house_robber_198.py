from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        prev_house1 = nums[0]
        prev_house2 = 0

        for i in range(1, n):
            current_max = max(prev_house1, prev_house2 + nums[i])
            prev_house2 = prev_house1
            prev_house1 = current_max

        return prev_house1


obj = Solution()
nums = [2, 7, 9, 3, 1]
print(obj.rob(nums))
