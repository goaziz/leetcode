from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for account in accounts:
            wealth_sum = sum(account)
            max_wealth = max(max_wealth, wealth_sum)

        return max_wealth


obj = Solution()
accounts = [[1, 5], [7, 3], [3, 5]]
print(obj.maximumWealth(accounts))
