class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for char in s:
            stack.append(char)

            if len(stack) >= len(part):
                if ''.join(stack[-len(part):]) == part:
                    del stack[-len(part):]

        return ''.join(stack)


obj = Solution()
s = "daabcbaabcbc"
part = "abc"
print(obj.removeOccurrences(s, part))
