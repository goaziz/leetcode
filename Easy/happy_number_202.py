class Solution:

    def sum_of_squre(self, x):
        s = 0
        while x > 0:
            dig = x % 10
            s += dig * dig
            x //= 10

        return s

    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_of_squre(n)

        return n == 1


obj = Solution()
n = 1111111
print(obj.isHappy(n))
