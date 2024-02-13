from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = heights.copy()
        expected.sort()

        for i, j in zip(heights, expected):
            if i != j:
                count += 1

        return count


obj = Solution()
heights = [1, 1, 4, 2, 1, 3]
print(obj.heightChecker(heights))
