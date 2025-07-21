from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        max_jump = 0

        while i < n:
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])
            i += 1

        return True


obj = Solution()
nums = [3, 2, 1, 0, 5]
print(obj.canJump(nums))
