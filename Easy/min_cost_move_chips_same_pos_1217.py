from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0

        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)


obj = Solution()
position = [1, 2, 3]
print(obj.minCostToMoveChips(position))
