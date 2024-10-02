from functools import reduce
import math
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = {}

        for d in deck:
            freq[d] = freq.get(d, 0) + 1

        values = freq.values()

        return reduce(math.gcd, values) >= 2


obj = Solution()
deck = [1, 2, 3, 4, 4, 3, 2, 1]
print(obj.hasGroupsSizeX(deck))
