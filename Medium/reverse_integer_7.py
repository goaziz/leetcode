class Solution:
    def reverse(self, x: int) -> int:
        is_negative = -1 if x < 0 else 1
        x *= is_negative

        s = 0
        while x != 0:
            dig = x % 10
            s = s * 10 + dig
            x //= 10

        s *= is_negative
        s_in_range = -2**31 <= s <= 2**31 - 1

        if not s_in_range:
            return 0
        else:
            return s

    def reverse2(self, x: int) -> int:
        s = str(abs(x))
        reversed_s = int(s[::-1])

        if reversed_s > 2 ** 31 - 1:
            return 0
        if x > 0:
            return reversed_s
        else:
            return reversed_s * -1


obj = Solution()
x = -120
print(obj.reverse(x))
