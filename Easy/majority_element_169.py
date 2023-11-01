from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i, j in c.items():
            if j > len(nums) // 2:
                return i

    def majorityElement2(self, nums: List[int]) -> int:
        n = len(nums)

        for i in nums:
            count = nums.count(i)
            if count > n // 2:
                return i

    def majorityElement3(self, nums: List[int]) -> int:
        count = 0
        majority_element = 0

        for i in nums:
            if count == 0:
                majority_element = i

            if majority_element == i:
                count += 1
            else:
                count -= 1

        return majority_element


obj = Solution()
nums = [3, 2, 3, 2, 2]
print(obj.majorityElement3(nums))
