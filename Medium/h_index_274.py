from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i, paper in enumerate(citations):
            if i + 1 <= paper:
                ans += 1
        
        return ans
        