from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        return count

    def subarraySum2(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        prefix_sum = 0
        hashmap[0] = 1
        count = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]

            hashmap[prefix_sum] += 1

        return count


obj = Solution()
nums = [1, 5, 3, 2]
k = 10
print(obj.subarraySum2(nums, k))
