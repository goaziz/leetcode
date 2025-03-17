from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix = 1
        for i in range(n - 1, -1, -1):
            prefix[i] *= suffix
            suffix *= nums[i]
        
        return prefix


obj = Solution()
nums = [5, 2, 3, 4]
print(obj.productExceptSelf(nums))
