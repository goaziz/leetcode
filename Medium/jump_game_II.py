from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        current_end = 0
        farthest = 0
        jump = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jump += 1
                current_end = farthest

        return jump


obj = Solution()
nums = [2, 3, 0, 1, 4]
print(obj.jump(nums))
