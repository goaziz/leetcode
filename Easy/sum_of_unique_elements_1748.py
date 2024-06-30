from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        sum_of_elements = 0

        for key, value in hashmap.items():
            if value == 1:
                sum_of_elements += key

        return sum_of_elements


obj = Solution()
nums = [1, 2, 3, 2]
print(obj.sumOfUnique(nums))
