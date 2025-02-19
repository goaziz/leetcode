from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        i = 0

        while len(nums) >= 2:
            num1 = nums.pop(0)
            num2 = nums.pop(0)
            sum_ = num1 + num2
            i += 1

            if i >= 2 and sum_ not in freq:
                break
            freq[sum_] += 1

        return next(iter(freq.values()))

    def maxOperations2(self, nums: List[int]) -> int:
        count = 1
        last_sum = nums[i] + nums[i + 1]

        for i in range(2, len(nums) - 1, 2):
            s = nums[i] + nums[i + 1]
            if s == last_sum:
                count += 1
            else:
                break

        return count


obj = Solution()
nums = [1, 5, 3, 3, 4, 1, 3, 2, 2, 3]
print(obj.maxOperations2(nums))
