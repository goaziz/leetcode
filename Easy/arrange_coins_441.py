class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            current = mid * (mid + 1) // 2

            if current == n:
                return mid
            elif n > current:
                left = mid + 1
            else:
                right = mid - 1

        return right

    def arrangeCoins2(self, n: int) -> int:
        count = 0
        i = 1

        while n >= 0:
            n -= i
            count += 1
            i += 1

        return count - 1


obj = Solution()
n = 5
print(obj.arrangeCoins2(n))
