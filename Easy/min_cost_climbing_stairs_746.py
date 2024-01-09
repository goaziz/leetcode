from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 1:
            return cost[0]

        dp = [0] * (n + 1)
        dp[1] = cost[0]
        dp[2] = cost[1]

        for step in range(3, n + 1):
            dp[step] = cost[step - 1] + min(dp[step - 1], dp[step - 2])

        return min(dp[n], dp[n - 1])


obj = Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(obj.minCostClimbingStairs(cost))
