class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        output = ''
        is_negative = False
        if num < 0:
            num = num * (-1)
            is_negative = True

        while num != 0:
            digit = num % 7
            output = output + str(digit)
            num //= 7

        if is_negative:
            return '-' + output[::-1]
        return output[::-1]


obj = Solution()
num = 25
print(obj.convertToBase7(num))
