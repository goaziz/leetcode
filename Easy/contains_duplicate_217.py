from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        count = 1

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                count += 1
            else:
                hashmap[i] = 1

            if count > 1:
                return True

        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for value in c.values():
            if value > 1:
                return True

        return False

    def containsDuplicate3(self, nums: List[int]) -> bool:

        hashmap = {}

        for i, j in enumerate(nums):
            if j in hashmap:
                return True

            hashmap[j] = i

        return False


obj = Solution()
nums = [1, 2, 3, 4, 3]
print(obj.containsDuplicate3(nums))
