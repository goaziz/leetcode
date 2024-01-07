from typing import List


class Solution:

    def divide_by_digit(self, n):
        temp = n

        while n > 0:
            digit = n % 10
            n //= 10

            if digit == 0:
                return False
            elif temp % digit != 0:
                return False 

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for i in range(left, right + 1):
            is_divisible_by_its_digits = self.divide_by_digit(i)
            if is_divisible_by_its_digits is True:
                result.append(i)

        return result


obj = Solution()
left = 47
right = 85
print(obj.selfDividingNumbers(left=left, right=right))
