from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        arr = []

        for i in range(len(prices)):
            is_exist = False
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    is_exist = True
                    diff = abs(prices[i] - prices[j])
                    arr.append(diff)
                    break

            if not is_exist:
                arr.append(prices[i])

        return arr

    def finalPrices2(self, prices: List[int]) -> List[int]:
        result = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]
            stack.append(i)

        return result


obj = Solution()
prices = [10, 1, 1, 6]
print(obj.finalPrices2(prices))
