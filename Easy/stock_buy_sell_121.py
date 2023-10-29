from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in prices[1:]:
            if max_profit < i:
                max_profit = max(max_profit, i - min_price)
            else:
                min_price = i

        return max_profit


obj = Solution()
prices = [2, 4, 1, 3, 8]
print(obj.maxProfit2(prices))
