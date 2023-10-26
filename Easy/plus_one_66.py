from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''
        l = []

        for i in digits:
            n += str(i)

        result = str(int(n) + 1)
        for i in result:
            l.append(int(i))

        return l

    def plusOne2(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits


obj = Solution()
digits = [1]
print(obj.plusOne2(digits))
