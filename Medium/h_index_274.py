from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i, paper in enumerate(citations):
            if i + 1 <= paper:
                ans += 1

        return ans

    def hIndex2(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0 for _ in range(n + 1)]

        for i, cite in enumerate(citations):
            if cite > n:
                counts[n] += 1
            else:
                counts[cite] += 1

        total = 0
        for i in range(n, -1, -1):
            total += counts[i]
            if total >= i:
                return i


obj = Solution()
citations = [3, 0, 6, 1, 5]
print(obj.hIndex2(citations))