import heapq
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        product1 = (nums[-1] - 1) * (nums[-2] - 1)

        return product1

    def maxProduct2(self, nums: List[int]) -> int:
        largest = heapq.nlargest(2, nums)

        return (largest[0] - 1) * (largest[1] - 1)

    def maxProduct3(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0

        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)

        return (biggest - 1) * (second_biggest - 1)


obj = Solution()
nums = [1, 5, 4, 5]
print(obj.maxProduct2(nums))
