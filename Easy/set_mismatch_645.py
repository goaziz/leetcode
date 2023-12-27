from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing_number = set(range(0, len(nums) + 1)).difference(set(nums))
        res = []

        for i, j in Counter(nums).items():
            if j > 1:
                res.append(i)

        res.append(list(missing_number)[1])
        return res

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for i in range(1, len(nums) + 1):
            if i in hashmap:
                if hashmap.get(i) == 2:
                    res.insert(0, i)
            else:
                res.insert(1, i)

        return res

    def findErrorNums3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_nums = n * (n + 1) // 2
        duplicate = sum(nums) - sum(set(nums))
        missing_number = sum_nums - sum(set(nums))

        return [duplicate, missing_number]


obj = Solution()
nums = [2, 2]
print(obj.findErrorNums3(nums))
