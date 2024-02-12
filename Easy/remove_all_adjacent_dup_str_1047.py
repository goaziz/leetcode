class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if len(stack) != 0:
                if stack[-1] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        return ''.join(stack)

    def removeDuplicates2(self, s: str) -> str:
        stack = []

        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)


obj = Solution()
s = "azxxzy"
print(obj.removeDuplicates2(s))
