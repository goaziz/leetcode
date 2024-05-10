from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for m in grid:
            for n in m:
                if n < 0:
                    count += 1

        return count

    def countNegatives2(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])

        for row in grid:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += (n - left)

        return count


obj = Solution()
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(obj.countNegatives2(grid))
