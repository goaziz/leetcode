class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for step in range(3, n + 1):
            dp[step] = dp[step - 1] + dp[step - 2]

        return dp[n]

    def climbStairs2(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        return self.climbStairs2(n - 1) + self.climbStairs2(n - 2)


obj = Solution()
print(obj.climbStairs2(3))
