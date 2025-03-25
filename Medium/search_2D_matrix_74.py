from typing import List


class Solution:

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return True

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for nums in matrix:
            exists = self.binary_search(nums, target)

            if exists:
                return True

        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        right = n * m - 1
        left = 0

        while left <= right:
            mid = (right + left) // 2
            row, col = divmod(mid, m)

            if matrix[row][col] == target:
                return True

            if matrix[row][col] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return False


obj = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(obj.searchMatrix2(matrix, target))
