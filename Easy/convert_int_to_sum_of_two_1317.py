from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        out = []

        for i in range(1, n):
            a = i
            b = n - i

            if a + b == n and ('0' not in str(a) and '0' not in str(b)):
                out = [a, b]

        return out

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            a, b = i, n - i

            if '0' not in str(a) and '0' not in str(b):
                return [a, b]


obj = Solution()
n = 13
print(obj.getNoZeroIntegers(n))
