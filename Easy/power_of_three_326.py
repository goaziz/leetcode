import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 3 != 0:
                return False

            n //= 3

        return True

    def isPowerOfThree2(self, n: int) -> bool:
        left = 0
        right = n // 3

        while left <= right:
            mid = left + (right - left) // 2
            temp = 3 ** mid
            if temp == n:
                return True
            elif temp > n:
                right = mid - 1
            else:
                left = mid + 1

        return False

    def isPowerOfThree3(self, n: int) -> bool:
        if n <= 0:
            return False

        root = math.log(n, 3)
        round_root = round(root, 1)

        if pow(3, round_root) == n:
            return True
        return False


obj = Solution()
print(obj.isPowerOfThree3(237))
