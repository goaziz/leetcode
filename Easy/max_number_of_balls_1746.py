from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sum_of_digits(n):
            s = 0

            while n != 0:
                digit = n % 10
                s += digit
                n //= 10
            return s

        hashmap = defaultdict(int)

        for i in range(lowLimit, highLimit + 1):
            sum_of_digit = sum_of_digits(i)
            hashmap[sum_of_digit] += 1

        return max(hashmap.values())


obj = Solution()
lowLimit = 5
highLimit = 15
print(obj.countBalls(lowLimit, highLimit))
