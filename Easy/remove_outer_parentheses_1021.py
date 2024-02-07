class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = []

        for i in s:
            if i == ')':
                count -= 1
            if count != 0:
                ans.append(i)
            if i == '(':
                count += 1

        return "".join(ans)


obj = Solution()
s = "(()())(())(()(()))"
print(obj.removeOuterParentheses(s))
