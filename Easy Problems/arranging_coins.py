class Solution:

    def arrangeCoins(self, n):
        return int((2 * n + 0.25) ** 0.5 - 0.5)


obj = Solution()
print(obj.arrangeCoins(25))
