class Solution:
    def minInsertions(self, s: str) -> int:
        open_needed = 0
        close_needed = 0

        for p in s:
            if p == '(':
                close_needed += 2
                if close_needed % 2 != 0:
                    open_needed += 1
                    close_needed -= 1
            else:
                close_needed -= 1
                if close_needed < 0:
                    open_needed += 1
                    close_needed = 1

        return open_needed + close_needed

    def minInsertions2(self, s: str) -> int:
        s = s.replace('))', '}')
        open_needed = 0
        close_needed = 0
        print(s)

        for p in s:
            if p == '(':
                close_needed += 2
            else:
                if p == ')':
                    open_needed += 1
                if close_needed:
                    close_needed -= 2
                else:
                    open_needed += 1

        return open_needed + close_needed


obj = Solution()
s = "(()))"
print(obj.minInsertions2(s))
