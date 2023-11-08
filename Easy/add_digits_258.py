import math


class Solution:

    def sum_of_digits(self, num):
        total = 0
        while num > 0:
            dig = num % 10
            total += dig
            num //= 10
        return total

    def addDigits(self, num: int) -> int:
        hashmap = {}

        while num not in hashmap:
            hashmap[num] = 1
            num = self.sum_of_digits(num)

        return num

    def addDigits2(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


obj = Solution()
print(obj.addDigits(0))
