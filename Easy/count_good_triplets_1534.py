import itertools
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    x = abs(arr[i] - arr[j])
                    y = abs(arr[j] - arr[k])
                    z = abs(arr[i] - arr[k])
                    if x <= a and y <= b and z <= c:
                        count += 1

        return count

    def countGoodTriplets2(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        for i, j, k in itertools.combinations(arr, 3):
            if abs(i - j) <= a and abs(j - k) <= b and abs(i - k) <= c:
                count += 1

        return count


obj = Solution()
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
print(obj.countGoodTriplets2(arr, a, b, c))
