from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        current_sum = 0
        min_length = float('inf')

        for end in range(len(nums)):
            current_sum += nums[end]

            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1

        return min_length if min_length != float('inf') else 0


obj = Solution()
target = 11
nums = [1, 2, 3, 4, 5]
print(obj.minSubArrayLen(target, nums))
