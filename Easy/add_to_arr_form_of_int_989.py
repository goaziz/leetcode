from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp = ''
        k = str(k)
        for n in num:
            temp += str(n)

        res = []
        carry = 0
        p1 = len(temp) - 1
        p2 = len(k) - 1

        while p1 >= 0 or p2 >= 0:
            x1 = ord(temp[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(k[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return res[::-1]


obj = Solution()
num = [2, 1, 5]
k = 806
print(obj.addToArrayForm2(num, k))
