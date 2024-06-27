class Solution:
    def totalMoney(self, n: int) -> int:
        primary, carry = divmod(n, 7)
        s = 0

        for i in range(primary):
            n = 7 + i
            current_sum = (n * (n + 1)) // 2
            actual_sum = (i * (i + 1)) // 2
            s += (current_sum - actual_sum)

        n = primary + carry
        current_sum = (n * (n + 1)) // 2
        actual_sum = (primary * (primary + 1)) // 2

        return s + (current_sum - actual_sum)

    def totalMoney2(self, n: int) -> int:
        s = 0
        m = 1

        while n > 0:
            for i in range(min(n, 7)):
                s += i + m

            n -= 7
            m += 1

        return s

    def totalMoney3(self, n: int) -> int:
        k, r = divmod(n, 7)
        a = 28
        b = a + (k - 1) * 7
        s = k * (a + b) // 2

        m = 1 + k
        final_week = 0
        for i in range(r):
            final_week += m + i

        return s + final_week

    def totalMoney4(self, n: int) -> int:
        w, r = divmod(n, 7)
        a = 28
        d = 7
        res = ((2 * a + d * (w - 1)) / 2) * w + sum(range(1, r + 1)) + w * r

        return int(res)


obj = Solution()
n = 10
print(obj.totalMoney3(n))
