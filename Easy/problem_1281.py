from functools import reduce
import operator


class Solution:

    def product_and_sum_of_digits(self, n):
        product = 1
        s = 0

        while n != 0:
            digit = n % 10
            product *= digit
            s += digit
            n //= 10

        return product - s

    def subtractProductAndSum(self, n: int) -> int:
        return self.product_and_sum_of_digits(n)

    def subtractProductAndSum2(self, n: int) -> int:
        s = 0
        product = 1

        for digit in str(n):
            product *= int(digit)
            s += int(digit)

        return product - s

    def subtractProductAndSum3(self, n: int) -> int:
        a = list(map(int, iter(str(n))))
        return reduce(lambda x, y: x * y, a) - reduce(lambda x, y: x + y, a)

    def subtractProductAndSum4(self, n: int) -> int:
        a = list(map(int, iter(str(n))))
        return reduce(operator.mul, a, 1) - reduce(operator.add, a, 0)


obj = Solution()
n = 4421
print(obj.subtractProductAndSum4(n))
