from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        def lower_bound(nums, target, start):
            left, right = start, len(nums)

            while left < right:
                mid = (right + left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        def upper_bound(nums, target, start):
            left, right = start, len(nums)

            while left < right:
                mid = (right + left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid

            return left

        count = 0
        n = len(nums)
        nums.sort()

        for i in range(n):
            low = lower_bound(nums, lower - nums[i], i + 1)
            high = upper_bound(nums, upper - nums[i], i + 1)
            count += high - low

        return count


obj = Solution()
nums = [0, 1, 7, 4, 4, 5]
lower = 3
upper = 6
print(obj.countFairPairs(nums, lower, upper))
