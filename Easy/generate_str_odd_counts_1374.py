class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            res = ['a'] * (n - 1) + ['b']
        else:
            res = ['a'] * n

        return ''.join(res)

    def generateTheString2(self, n: int) -> str:
        s = ['a', 'b']

        if n % 2 == 0:
            return s[0] * (n - 1) + s[1]
        else:
            return s[0] * n


obj = Solution()
n = 4
print(obj.generateTheString(n))
