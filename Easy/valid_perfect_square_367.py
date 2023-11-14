from math import sqrt


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid < num:
                low = mid + 1
            elif mid * mid > num:
                high = mid - 1
            else:
                return True
        return False

    def isPerfectSquare2(self, num: int) -> bool:
        temp = int(num ** 0.5)
        if temp * temp == num:
            return True
        return False

    def isPerfectSquare3(self, num: int) -> bool:
        return sqrt(num).is_integer()


obj = Solution()
print(obj.isPerfectSquare(25))
