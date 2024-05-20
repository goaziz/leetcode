from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        nums.sort(reverse=True)
        arr = [nums[0]]

        for i in range(1, len(nums)):
            if sum(arr) <= sum(nums[i:]):
                arr.append(nums[i])

        return arr

    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        arr = []
        total = sum(nums)
        current_sum = 0

        for num in nums:
            total -= num
            current_sum += num
            arr.append(num)

            if current_sum > total:
                return arr


obj = Solution()
nums = [4, 3, 10, 9, 8]
print(obj.minSubsequence(nums))
