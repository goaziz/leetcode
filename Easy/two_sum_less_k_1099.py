from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_n = -1

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s < k:
                    max_n = max(max_n, s)

        return max_n

    def twoSumLessThanK2(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = len(nums) - 1
        left = 0
        max_n = -1

        while left < right:
            s = nums[left] + nums[right]

            if s < k:
                left += 1
                max_n = max(s, max_n)
            else:
                right -= 1

        return max_n


obj = Solution()
nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60
print(obj.twoSumLessThanK2(nums, k))
