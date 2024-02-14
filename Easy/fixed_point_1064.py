from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for idx, val in enumerate(arr):
            if idx == val:
                return idx

        return -1

    def fixedPoint2(self, arr: List[int]) -> int:
        # Initialize the boundary of search space
        left, right = 0, len(arr) - 1

        # Initialize answer to -1,
        # If no answer is possible, we will return -1
        answer = -1

        # While the boundary size is non zero
        while left <= right:
            # The middle point in the search space
            # To divide the search space into two halves
            mid = (left + right) // 2

            if arr[mid] == mid:
                # We found a possible answer, but keep looking
                # for a smaller index on the left part
                answer = mid
                right = mid - 1
            elif arr[mid] < mid:
                # No solution possible on left, move to the right half
                left = mid + 1
            else:
                # No solution possible on right, move to the left half
                right = mid - 1

        return answer


obj = Solution()
arr = [-10, -5, 3, 4, 7, 9]
print(obj.fixedPoint(arr))
