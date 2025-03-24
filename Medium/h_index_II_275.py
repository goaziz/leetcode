from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        n = len(citations)

        while left <= right:
            mid = left + (right - left) // 2
            h = n - mid
            
            if h <= citations[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return n - left


obj = Solution()
citations = [0, 1, 3, 5, 6]
print(obj.hIndex(citations))
