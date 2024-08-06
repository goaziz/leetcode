from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n - 1):
            actual_idx = i % n
            while stack and nums[stack[-1]] < nums[actual_idx]:
                idx = stack.pop()
                ans[idx] = nums[actual_idx]

            if i < n:
                stack.append(i)

        return ans


obj = Solution()
nums = [5, 4, 3, 2, 1]
print(obj.nextGreaterElements(nums))
