class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        res = ''
        count = 0

        for i in s[::-1]:
            if count == 3:
                res += '.'
                res += i
                count = 0
            else:
                res += i
            count += 1

        return res[::-1]

    def thousandSeparator2(self, n: int) -> str:
        s = str(n)
        count = 0
        res = ''

        for i in range(len(s) - 1, -1, -1):
            res += s[i]
            count += 1
            if count % 3 == 0 and i != 0:
                res += '.'

        return res[::-1]

    def thousandSeparator3(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")


obj = Solution()
n = 100
print(obj.thousandSeparator3(n))
