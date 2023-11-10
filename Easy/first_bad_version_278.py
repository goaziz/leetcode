# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n + 1

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid + 1
            else:
                left = mid

        return left
