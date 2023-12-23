from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s = list(set(nums))
        hashmap = Counter(nums)
        s.sort(reverse=True)
        max_count = 0

        for i in range(len(s) - 1):
            diff = s[i] - s[i + 1]
            if diff == 1:
                sum_of_keys = hashmap[s[i]] + hashmap[s[i + 1]]
                max_count = max(sum_of_keys, max_count)

        return max_count

    def findLHS2(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        max_count = 0

        for num in nums:
            if num + 1 in hashmap:
                max_count = max(max_count, hashmap[num] + hashmap[num + 1])
            if num - 1 in hashmap:
                max_count = max(max_count, hashmap[num] + hashmap[num - 1])

        return max_count


obj = Solution()
print(obj.findLHS2(nums=[1, 3, 2, 2, 5, 2, 3, 7]))
print(obj.findLHS2(nums=[1, 2, 3, 4]))
print(obj.findLHS2(nums=[1, 1, 1, 1]))
