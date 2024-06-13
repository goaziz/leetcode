import math
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        elements = int(0.05 * len(arr))
        arr = arr[elements: -elements]
        mean = sum(arr) / len(arr)

        return round(mean, 5)


obj = Solution()
arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]
print(obj.trimMean(arr))
