class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        idx = 0
        res = ''
        sign = 1
        int_max = pow(2, 31) - 1
        int_min = -pow(2, 31)

        while idx < n and s[idx] == ' ':
            idx += 1

        if idx < n and s[idx] in ['+', '-']:
            sign = eval(s[idx] + '1')
            idx += 1

        while idx < n and s[idx].isdigit():
            res += s[idx]
            idx += 1

        return min(int_max, max(int_min, sign * int(res))) if res else 0


obj = Solution()
s = "    -42"
print(obj.myAtoi(s))
