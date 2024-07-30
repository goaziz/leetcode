from typing import List


class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        nums.append(float('inf'))
        stack = []

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                s = i - stack[-1] - 1 if stack else i
                ans[j] = s
            stack.append(i)

        return ans


obj = Solution()
nums = [1, 5, 4, 3, 6]
print(obj.maximumLengthOfRanges(nums))
