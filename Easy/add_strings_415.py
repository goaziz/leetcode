

import sys


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(0)
        a, b = 0, 0

        for i in num1:
            digit = ord(i) - 48
            a *= 10
            a += digit

        for i in num2:
            digit = ord(i) - 48
            b *= 10
            b += digit

        return str(a + b)

    def addStrings2(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1

        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])


obj = Solution()
num1 = '99'
num2 = '231'
print(obj.addStrings2(num1, num2))
