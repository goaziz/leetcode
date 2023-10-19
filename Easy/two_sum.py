from typing import List


class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)

        for i in range(l - 1):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Better solution

class Solution2:
    # Time: O(n)
    # Space: O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, j in enumerate(nums):
            difference = target - j

            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[nums[i]] = i
