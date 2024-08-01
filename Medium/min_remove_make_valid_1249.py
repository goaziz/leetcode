class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes = []
        n = len(s)
        stack = []

        for i in range(n):
            if s[i] == ')' and stack and stack[-1] == '(':
                stack.pop()
                indexes.pop()
            elif s[i] == '(' or s[i] == ')':
                stack.append(s[i])
                indexes.append(i)

        set_index = set(indexes)
        ans = ""

        for i in range(n):
            if i not in set_index:
                ans += s[i]

        return ans

    def minRemoveToMakeValid2(self, s: str) -> str:
        n = len(s)
        indexes = set()
        stack = []

        for i in range(n):
            if s[i] not in '()':
                continue
            if s[i] == '(':
                stack.append(i)
            elif not stack:
                indexes.add(i)
            else:
                stack.pop()

        indexes = indexes.union(set(stack))
        ans = ""
        for i in range(n):
            if i not in indexes:
                ans += s[i]

        return ans


obj = Solution()
s = "))(("
print(obj.minRemoveToMakeValid(s))
