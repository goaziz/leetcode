from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = 0
        ans = []

        for s in seq:
            if s == '(':
                ans.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                ans.append(depth % 2)

        return ans


obj = Solution()
seq = "()(())()"
print(obj.maxDepthAfterSplit(seq))
