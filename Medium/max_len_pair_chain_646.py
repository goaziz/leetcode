from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        count = 0
        curr_end = float('-inf')

        for left, right in pairs:
            if left > curr_end:
                curr_end = right
                count += 1

        return count


obj = Solution()
pairs = [[1, 2], [7, 8], [4, 5]]
print(obj.findLongestChain(pairs))
