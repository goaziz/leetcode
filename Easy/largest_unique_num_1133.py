from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        max_num = -1

        for key, val in hashmap.items():
            if val == 1 and key > max_num:
                max_num = key

        return max_num


obj = Solution()
nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(obj.largestUniqueNumber(nums))
