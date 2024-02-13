class Solution:
    def confusingNumber(self, n: int) -> bool:
        numbers = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        res = []
        for s in str(n):
            if s not in numbers:
                return False
            res.append(numbers.get(s))

        combined = ''.join(res)
        return int(combined[::-1]) != n

    def confusingNumber2(self, n: int) -> bool:
        numbers = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }

        temp = n
        a = 0

        while temp:
            remainder = temp % 10
            if remainder not in numbers:
                return False

            a = a * 10 + numbers.get(remainder)
            temp //= 10

        return a != n


obj = Solution()
n = 68
print(obj.confusingNumber(n))
