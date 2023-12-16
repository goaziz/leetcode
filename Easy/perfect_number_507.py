class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 != 0:
            return False

        total = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                total += i

        return num == total

    def checkPerfectNumber2(self, num: int) -> bool:
        if num <= 0:
            return False

        total = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i + num // i

        return total == num


obj = Solution()
print(obj.checkPerfectNumber2(99999995))
print(obj.checkPerfectNumber2(28))
print(obj.checkPerfectNumber2(7))