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

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        minimum_cost = [0] * (len(cost) + 1)

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i - 1] + cost[i - 1]
            take_two_steps = minimum_cost[i - 2] + cost[i - 2]
            minimum_cost[i] = min(take_one_step, take_two_steps)

        # The final element in minimum_cost refers to the top floor
        return minimum_cost[-1]

    def minCostClimbingStairs3(self, cost: List[int]) -> int:
        down_one = down_two = 0
        for i in range(2, len(cost) + 1):
            temp = down_one
            down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
            down_two = temp

        return down_one


obj = Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(obj.minCostClimbingStairs3(cost))
