from collections import Counter
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        rank = 1
        ranks = {}

        for num in sorted_arr:
            if num not in ranks:
                ranks[num] = rank
                rank += 1

        res = [ranks[num] for num in arr]
        return res

    def arrayRankTransform2(self, arr: List[int]) -> List[int]:
        ranks = {}
        rank = 1

        for num in sorted(list(set(arr))):
            ranks[num] = rank
            rank += 1

        return [ranks[num] for num in arr]


obj = Solution()
arr = [100, 100, 100]
print(obj.arrayRankTransform2(arr))
