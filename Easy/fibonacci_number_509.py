class Solution:

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for step in range(2, n + 1):
            dp[step] = dp[step - 1] + dp[step - 2]

        return dp[n]

    def fib2(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        return self.fib2(n - 1) + self.fib2(n - 2)


obj = Solution()
print(obj.fib(2))
print(obj.fib(3))
print(obj.fib(4))
