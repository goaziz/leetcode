class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n /= 2

        while n % 3 == 0:
            n /= 3

        while n % 5 == 0:
            n /= 5

        return n == 1

    def isUgly2(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n = n // i

        return n == 1


obj = Solution()
print(obj.isUgly(6))
