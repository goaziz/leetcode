from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n

        for i in range(n):
            arr[i] = sum(nums[:i + 1])

        return arr

    def runningSum2(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        return nums


obj = Solution()
nums = [1, 2, 3, 4]
print(obj.runningSum2(nums))
