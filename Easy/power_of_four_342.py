import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 4 != 0:
                return False

            n //= 4

        return True

    def isPowerOfFour2(self, n: int) -> bool:
        if n <= 0:
            return False

        root = math.log(n, 4).is_integer()

        if root:
            return True
        return False


obj = Solution()
print(obj.isPowerOfFour2(16))
