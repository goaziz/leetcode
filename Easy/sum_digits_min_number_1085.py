from typing import List


class Solution:

    def sum_digits(self, n):
        total = 0

        while n != 0:
            dig = n % 10
            total += dig
            n //= 10

        return total

    def sumOfDigits(self, nums: List[int]) -> int:
        min_number = min(nums)
        s = self.sum_digits(min_number)

        if s % 2 == 0:
            return 1
        else:
            return 0


obj = Solution()
nums = [34, 23, 1, 24, 75, 33, 54, 8]
print(obj.sumOfDigits(nums))
