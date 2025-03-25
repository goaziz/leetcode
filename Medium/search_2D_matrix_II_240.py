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