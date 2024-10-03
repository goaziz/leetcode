from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        children = len(g)
        cookies = len(s)
        i, j = 0, 0

        while children > i and cookies > j:
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i


obj = Solution()
g = [1, 2, 3]
s = [1, 1]
print(obj.findContentChildren(g, s))
