class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 0 or sum > 9 * num:
            return ""

        digits = []
        for _ in range(num):
            d = min(9, sum)
            digits.append(d)
            sum -= d

        return "".join(str(d) for d in digits)


obj = Solution()
num = 2
sum = 3
print(obj.maxSumOfSquares(num, sum))
