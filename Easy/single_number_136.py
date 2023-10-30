from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)

        for i, j in c.items():
            if j == 1:
                return i

    def singleNumber2(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

    def singleNumber3(self, nums: List[int]) -> int:
        seen = set()

        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)

        for s in seen:
            return s

    # under development
    # def singleNumber4(self, nums: List[int]) -> int:
    #     hashmap = {}
    #     for i in nums:
    #         if i in hashmap:
    #             hashmap[i] += 1
    #         else:
    #             hashmap[i] = 1
    #
    #     print(hashmap.keys())
    #     for val in hashmap.values():
    #         if val == 1:
    #             return hashmap[val]


obj = Solution()
nums = [1, 2, 1, 2, 3]
print(obj.singleNumber4(nums))
