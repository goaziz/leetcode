class Solution:
    def isArmstrong(self, n: int) -> bool:
        exp = len(str(n))
        temp = n
        result = 0

        while n != 0:
            base = n % 10
            result += pow(base, exp)
            n //= 10

        return temp == result


obj = Solution()
n = 123
print(obj.isArmstrong(n))
