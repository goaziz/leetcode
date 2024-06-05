from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ''

        for i in range(len(s)):
            idx = indices.index(i)
            ans += s[idx]

        return ans


obj = Solution()
s = "abc"
indices = [0, 1, 2]
print(obj.restoreString(s, indices))
