import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m + n - 2
        r = m - 1
        #  formual N! / (r!(N - r)!)

        res = math.factorial(N) // (math.factorial(r) * math.factorial(N - r))

        return res

    def uniquePaths2(self, m: int, n: int) -> int:
        N = m + n - 2
        r = min(n - 1, m - 1)

        if r == 0:
            return 1

        res = 1
        for i in range(1, r + 1):
            res = res * (N - r + i) // i

        return res

    def uniquePaths3(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                dp[col][row] = dp[col - 1][row] + dp[col][row - 1]

        return dp[m - 1][n - 1]


obj = Solution()
m = 3
n = 7
print(obj.uniquePaths3(m, n))
