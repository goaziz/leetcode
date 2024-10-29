from itertools import combinations
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        s = nums[a] + nums[b] + nums[c]

                        if s == nums[d]:
                            count += 1

        return count

    def countQuadruplets2(self, nums: List[int]) -> int:
        result = 0
        comb = combinations(nums, r=4)
        for comb_tuple in comb:
            if comb_tuple[0] + comb_tuple[1] + comb_tuple[2] == comb_tuple[3]:
                result += 1
        return result


obj = Solution()
nums = [1, 1, 1, 3, 5]
print(obj.countQuadruplets(nums))
