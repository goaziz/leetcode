import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 2 != 0:
                return False

            n //= 2

        return True

    def isPowerOfTwo2(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log2(n) % 1 == 0


obj = Solution()
n = 32
print(obj.isPowerOfTwo(n))
