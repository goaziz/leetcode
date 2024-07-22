class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if char == 'B':
                if stack and stack[-1] == 'A':
                    stack.pop()
                else:
                    stack.append(char)
            elif char == 'D':
                if stack and stack[-1] == 'C':
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return len(stack)

    def minLength2(self, s: str) -> int:
        stack = []

        for char in s:
            if stack and stack[-1] + char in ['AB', 'CD']:
                stack.pop()
            else:
                stack.append(char)

        return len(stack)


obj = Solution()
s = "ABFCACDB"
print(obj.minLength(s))
