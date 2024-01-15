from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idx = s.index(c)
        ans = []
        
        for index, val in enumerate(s):
            if val == c:
                idx = index
            ans.append(abs(idx - index))

        idx = float('inf')  # Reset idx to positive infinity
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], abs(i - idx))
        return ans


obj = Solution()
s = "loveleetcode"
c = "e"
print(obj.shortestToChar(s, c))
