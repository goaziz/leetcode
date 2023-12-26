import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        product1 = nums[0] * nums[1] * nums[n - 1]
        product2 = nums[n - 1] * nums[n - 2] * nums[n - 3]

        return max(product1, product2)

    def maximumProduct2(self, array):
        largest = heapq.nlargest(3, array)
        smallest = heapq.nsmallest(2, array)

        return max(largest[0] * largest[1] * largest[2], largest[0] * smallest[0] * smallest[1])


obj = Solution()
# nums = [-1, -2, -3, -4]
nums = [-100, -98, -1, 2, 3, 4]
print(obj.maximumProduct(nums))
