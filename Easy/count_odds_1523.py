class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low = low if low % 2 != 0 else low + 1
        high = high if high % 2 != 0 else high - 1

        if low > high:
            return 0

        return (high - low) // 2 + 1

    def countOdds2(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        return (high - low) // 2 + 1


obj = Solution()
low = 3
high = 7
print(obj.countOdds(low, high))
